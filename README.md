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

## YouTube Authentication

The system includes a YouTube authentication module that helps manage YouTube cookies for better access to YouTube content. This is particularly useful for handling age-restricted content and improving overall YouTube access.

### Features
- Automated cookie management
- Secure cookie storage
- Login verification
- Error handling and logging

### Usage
1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the authentication script:
```bash
python -m cookies.youtube_auth
```

3. Follow the on-screen instructions to:
   - Enter a name for your cookie file
   - Log in to your YouTube account
   - Complete the authentication process

The cookies will be saved in the `cookies` directory and can be used by the system for YouTube operations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, join our [Telegram Support Group](https://t.me/zefronmusic). 