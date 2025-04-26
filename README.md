# ZefMusic Bot

A feature-rich Telegram music bot for playing music in group voice chats.

## Features

- Play music from YouTube
- Support for voice chats
- Queue system
- Admin commands
- User-friendly interface
- Modern and clean design

## Requirements

- Python 3.8 or higher
- A Telegram Account
- A Telegram Bot Token
- MongoDB Database

## Installation

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/Suraj08832/musiccbot.git
cd musiccbot
```

2. Install the requirements:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your credentials:
```env
BOT_TOKEN=your_bot_token
MONGO_DB_URI=your_mongodb_uri
API_ID=your_api_id
API_HASH=your_api_hash
BOT_USERNAME=your_bot_username
OWNER_ID=your_telegram_id
```

4. Run the bot:
```bash
python -m ZEFMUSIC
```

### Koyeb Deployment

1. Fork this repository
2. Create a Koyeb account at https://app.koyeb.com
3. Click on "Create App"
4. Select "GitHub" as deployment method
5. Select your forked repository
6. Configure the following environment variables:
   - `BOT_TOKEN`
   - `MONGO_DB_URI`
   - `API_ID`
   - `API_HASH`
   - `BOT_USERNAME`
   - `OWNER_ID`
7. Click "Deploy"

## Commands

- `/play` - Play music from YouTube
- `/pause` - Pause the current track
- `/resume` - Resume the paused track
- `/skip` - Skip to the next track
- `/stop` - Stop the playback
- `/queue` - Show the current queue
- `/addsudo` - Add a user as sudo (Owner only)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, join our [Telegram Support Group](https://t.me/zefronmusic). 