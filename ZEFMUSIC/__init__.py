import sys
import os
import logging
from config import BOT_USERNAME, OWNER_ID
from datetime import datetime
from logging.handlers import RotatingFileHandler
import time

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(
            "zefmusic.log", maxBytes=50000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

# Bot start time
bot_start_time = time.time()

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import test configuration
import config

from ZEFMUSIC.core.bot import KINGBot
from ZEFMUSIC.core.dir import dirr
from ZEFMUSIC.core.git import git
from ZEFMUSIC.core.userbot import Userbot
from ZEFMUSIC.misc import dbb

from .logging import LOGGER

dirr()

try:
    git()
except ImportError:
    git = None
    LOGGER.warning("Git module not found. Some features may be limited.")

dbb()

app = KINGBot()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

from ZEFMUSIC.core.mongo import mongodb
from ZEFMUSIC.core.call import Call
from ZEFMUSIC.misc import sudo
from ZEFMUSIC.utils import time_to_seconds
from ZEFMUSIC.utils.decorators import language
from ZEFMUSIC.utils.extraction import extract_user
from ZEFMUSIC.utils.formatters import get_readable_time
from ZEFMUSIC.utils.inline import help_pannel
from ZEFMUSIC.utils.pastebin import KINGBin
from ZEFMUSIC.utils.stream.stream import stream
from ZEFMUSIC.utils.thumbnails import get_thumb
from ZEFMUSIC.utils.ytdl import ytdl