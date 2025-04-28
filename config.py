import re
from os import getenv
import os

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "11550139"))
API_HASH = getenv("API_HASH", "75080c7b5c6503ad1309a19e055f1524")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7680697190:AAGk1LWo6tlwOopZ10JOLwwHU4Zd_y6IWNQ")

# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "radharani_musicbot")

# Get Your repo
REPO_LINK = getenv("REPO_LINK", "https://t.me/radharani_musicbot")

# Don't Add style font 
BOT_NAME = getenv("BOT_NAME", "Radharani Music Bot")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://rekhasharma13061990:ubEl6ILtVpZr4HLV@cluster0.t86veax.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002605198416"))

# Get this value from @CrewMusic_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7694579428"))

# Sudo users
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "7672710416").split()))

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sandeephere08/ZEFMUSIC"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ZEFRONAssociation")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/zefronmusic")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQCwPbsAH5Yh_Pb4-L7Rrcv7lA9AhhYsV9J9uR2aa_pnNPwfh-1Ka_VMGhCsNDNKOsLdgoR3aZzaQ9rO24edu9VgwdwoeQXpYHQpu3CreiD_KnNrN7bF5zRGOXVTARBr9jsw3rb3YQiFdsul3iloa7d6fyFrmVoBRgVnAgl3CSoKF3a2tPsiV9JG3azmA11Abavj45oC5dbNKDYQOoon68kZJGomrrcH4XDDLAZ2m2Ej74fGDxNfd8h_aLJ6R8NZhvr70T6r3z06zMTKZiDanhsEtUeBRGjy6O1pAH-SIOWF-NMY0Re6_tXgux07UcBHKEaR6B7GYf2S8a8DTDIPGaiB_W7J-AAAAAHKofbkAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/2e2f78610814092d61103.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/ce5ffb3d5f383c781f234.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
