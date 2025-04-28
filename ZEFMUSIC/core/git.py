import asyncio
import shlex
from typing import Tuple
import os
import sys
from config import UPSTREAM_REPO, UPSTREAM_BRANCH

try:
    from git import Repo
    from git.exc import GitCommandError, InvalidGitRepositoryError
    git = True
except ImportError:
    git = False

import config

from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def get_git_repo():
    if not git:
        return None
    
    try:
        repo = Repo()
        return repo
    except Exception as e:
        LOGGER.warning(f"Failed to get git repo: {str(e)}")
        return None

def get_git_remote():
    if not git:
        return None
    
    try:
        repo = get_git_repo()
        if repo:
            return repo.remote("origin")
        return None
    except Exception as e:
        LOGGER.warning(f"Failed to get git remote: {str(e)}")
        return None

def get_git_branch():
    if not git:
        return None
    
    try:
        repo = get_git_repo()
        if repo:
            return repo.active_branch.name
        return None
    except Exception as e:
        LOGGER.warning(f"Failed to get git branch: {str(e)}")
        return None

def get_git_commit():
    if not git:
        return None
    
    try:
        repo = get_git_repo()
        if repo:
            return repo.head.commit.hexsha
        return None
    except Exception as e:
        LOGGER.warning(f"Failed to get git commit: {str(e)}")
        return None

def git():
    if not git:
        LOGGER.warning("Git module not found. Some features may be limited.")
        return

    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    try:
        repo = Repo()
        LOGGER.info("Git Client Found [VPS DEPLOYER]")
    except (GitCommandError, InvalidGitRepositoryError) as e:
        LOGGER.warning(f"Git repository not found: {str(e)}")
        try:
            repo = Repo.init()
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
            else:
                origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()
            repo.create_head(
                config.UPSTREAM_BRANCH,
                origin.refs[config.UPSTREAM_BRANCH],
            )
            repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
                origin.refs[config.UPSTREAM_BRANCH]
            )
            repo.heads[config.UPSTREAM_BRANCH].checkout(True)
            try:
                repo.create_remote("origin", config.UPSTREAM_REPO)
            except BaseException as e:
                LOGGER.warning(f"Failed to create remote: {str(e)}")
            nrs = repo.remote("origin")
            nrs.fetch(config.UPSTREAM_BRANCH)
            try:
                nrs.pull(config.UPSTREAM_BRANCH)
            except GitCommandError:
                repo.git.reset("--hard", "FETCH_HEAD")
            LOGGER.info("Fetching updates from upstream repository...")
        except Exception as e:
            LOGGER.error(f"Error in git setup: {str(e)}")
            return
