import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp
from keep_alive import keep_alive

# Load environment variables
load_dotenv()

# Start keep alive server
keep_alive()

# Initialize the bot
bot = Client(
    "ZefMusic",
    api_id=os.getenv("API_ID", "11550139"),
    api_hash=os.getenv("API_HASH", "75080c7b5c6503ad1309a19e055f1524"),
    bot_token=os.getenv("BOT_TOKEN", "7680697190:AAGk1LWo6tlwOopZ10JOLwwHU4Zd_y6IWNQ")
)

# Initialize PyTgCalls
call_py = PyTgCalls(bot)

# Store active voice chats
active_chats = {}

@bot.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Support", url=os.getenv("SUPPORT_CHAT", "https://t.me/zefronmusic")),
                InlineKeyboardButton("Channel", url=os.getenv("SUPPORT_CHANNEL", "https://t.me/ZEFRONAssociation"))
            ]
        ]
    )
    await message.reply_photo(
        photo=os.getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg"),
        caption="🎵 Welcome to ZefMusic Bot!\n\nI'm your personal music companion. Use /play to enjoy music in voice chat.\n\nCreated by @ZefMusic",
        reply_markup=keyboard
    )

@bot.on_message(filters.command("play"))
async def play_command(client: Client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        await message.reply("🎵 Please provide a song name or reply to an audio file.")
        return

    try:
        # Get the chat where the command was sent
        chat_id = message.chat.id
        
        # Check if user is in a voice chat
        if not message.from_user.voice:
            await message.reply("🎵 Please join a voice chat first!")
            return

        # Join the voice chat
        voice_chat = await message.from_user.voice.chat.join()
        active_chats[chat_id] = voice_chat

        # If replying to an audio file
        if message.reply_to_message and message.reply_to_message.audio:
            audio = message.reply_to_message.audio
            await message.reply("🎵 Playing audio...")
            await voice_chat.play_audio(audio.file_id)
        else:
            # Search and play from YouTube
            query = " ".join(message.command[1:])
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
                url = info['url']
                title = info['title']
                
            await message.reply(f"🎵 Playing: {title}\n\nPowered by ZefMusic")
            await voice_chat.play_audio(url)

    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")

@bot.on_message(filters.command("stop"))
async def stop_command(client: Client, message: Message):
    chat_id = message.chat.id
    if chat_id in active_chats:
        await active_chats[chat_id].leave()
        del active_chats[chat_id]
        await message.reply("🎵 Stopped playing and left voice chat.\n\nThanks for using ZefMusic!")
    else:
        await message.reply("🎵 No active voice chat in this group.")

@bot.on_message(filters.command("ping"))
async def ping_command(client: Client, message: Message):
    await message.reply_photo(
        photo=os.getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg"),
        caption="🎵 Pong! ZefMusic Bot is alive and working perfectly!"
    )

# Start the bot
if __name__ == "__main__":
    print("🎵 Starting ZefMusic Bot...")
    bot.run() 