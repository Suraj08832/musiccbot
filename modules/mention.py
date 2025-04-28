import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant

from ZEFMUSIC import app
from ZEFMUSIC.utils import admin_filter

SPAM_CHATS = []

@app.on_message(filters.command(["mention", "all"]) & filters.group & admin_filter)
async def tag_all_users(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")

    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply("๏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ")

    if chat_id in SPAM_CHATS:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")

    SPAM_CHATS.append(chat_id)
    usernum = 0
    usertxt = ""

    try:
        if message.reply_to_message:
            async for m in client.get_chat_members(chat_id):
                if chat_id not in SPAM_CHATS:
                    break
                if m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 5:
                    await message.reply_to_message.reply_text(usertxt)
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
        else:
            text = message.text.split(None, 1)[1]
            async for m in client.get_chat_members(chat_id):
                if chat_id not in SPAM_CHATS:
                    break
                if m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 5:
                    await client.send_message(
                        chat_id,
                        f"{text}\n{usertxt}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /alloff ||"
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
    except Exception as e:
        print(f"Error in tag_all_users: {e}")
    finally:
        try:
            SPAM_CHATS.remove(chat_id)
        except:
            pass

@app.on_message(filters.command("alloff") & ~filters.private)
async def cancelcmd(client, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except:
            pass
        return await message.reply_text("๏ ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!")
    else:
        return await message.reply_text("๏ ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!") 