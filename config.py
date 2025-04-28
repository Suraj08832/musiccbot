import re
from os import getenv
import os

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 27359357
API_HASH = "cf2a75861140ceb746c7796e07cbf1d5"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "6769894527:AAFpwQhGhF5QZBxwYFJGOPxQPPvYz_Hy_Hs"

# Get Your bot username
BOT_USERNAME = "systummusic_bot"

# Get Your repo
REPO_LINK = "https://github.com/AnonymousX1025/AnonXMusic"

# Don't Add style font 
BOT_NAME = "Systum Music"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb://localhost:27017/zefmusic"

DURATION_LIMIT_MIN = 180

# Chat id of a group for logging bot's activities
LOGGER_ID = -1001919707080

# Get this value from @CrewMusic_bot on Telegram by /id
OWNER_ID = 6299128233

# Sudo users
SUDO_USERS = [6299128233]

UPSTREAM_REPO = "https://github.com/AnonymousX1025/AnonXMusic"
UPSTREAM_BRANCH = "master"
GIT_TOKEN = getenv("GIT_TOKEN")

SUPPORT_CHANNEL = "https://t.me/FallenAssociation"
SUPPORT_CHAT = "https://t.me/DevilsHeavenMF"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Get your pyrogram v2 session from @StringSessionBot on Telegram
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG")
PING_IMG_URL = getenv("PING_IMG")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG")
STATS_IMG_URL = getenv("STATS_IMG")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO")
STREAM_IMG_URL = getenv("STREAM_IMG")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG")

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

def validate_url(url):
    if not url:
        return True
    if not re.match("(?:http|https)://", url):
        return False
    return True

if not validate_url(SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
    )

if not validate_url(SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
    )