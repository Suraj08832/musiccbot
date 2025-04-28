from ZEFMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [
    "🦋🦋🦋🦋🦋",
    "🧚🌸🧋🍬🫖",
    "🥀🌷🌹🌺💐",
    "🌸🌿💮🌱🌵",
    "❤️💚💙💜🖤",
    "💓💕💞💗💖",
    "🌸💐🌺🌹🦋",
    "🍔🦪🍛🍲🥗",
    "🍎🍓🍒🍑🌶️",
    "🧋🥤🧋🥛🍷",
    "🍬🍭🧁🎂🍡",
    "🍨🧉🍺☕🍻",
    "🥪🥧🍦🍥🍚",
    "🫖☕🍹🍷🥛",
    "☕🧃🍩🍦🍙",
    "🍁🌾💮🍂🌿",
    "🌨️🌥️⛈️🌩️🌧️",
    "🌷🏵️🌸🌺💐",
    "💮🌼🌻🍀🍁",
    "🧟🦸🦹🧙👸",
    "🧅🍠🥕🌽🥦",
    "🐷🐹🐭🐨🐻‍❄️",
    "🦋🐇🐀🐈🐈‍⬛",
    "🌼🌳🌲🌴🌵",
    "🥩🍋🍐🍈🍇",
    "🍴🍽️🔪🍶🥃",
    "🕌🏰🏩⛩️🏩",
    "🎉🎊🎈🎂🎀",
    "🪴🌵🌴🌳🌲",
    "🎄🎋🎍🎑🎎",
    "🦅🦜🕊️🦤🦢",
    "🦤🦩🦚🦃🦆",
    "🐬🦭🦈🐋🐳",
    "🐔🐟🐠🐡🦐",
    "🦩🦀🦑🐙🦪",
    "🐦🦂🕷️🕸️🐚",
    "🥪🍰🥧🍨🍨",
    "🥬🍉🧁🧇",
]

TAGMES = [
    "Hey Cool Angel Kaha Ho🤗🥱",
    "Oye So Gye Kya Online Aao😊",
    "Vc Chalo Baten Karte Hain Kuch Kuch😃",
    "ALOK Khana Kha Liye Ji ..??🥲",
    "Ghar Me Sab Kaisa Hai Ji🥺",
    "Pta Hai Bohot Miss Kar Rhi Thi Aapko🤭",
    "Oye Hal Chal Kesa Hai..??🤨",
    "Setting Karwa Doge..??🙂",
    "Aapka Name Kya hai..??🥲",
    "Nasta Hua Aapka..??😋",
    "Mere Ko Apne Group Me Add Kr Lo😍",
    "Aapki Partner Aapko Dhund Rhe Hain Jldi Online Ayaie😅😅",
    "Mere Se Dosti Kroge..??🤔",
    "Sone Chal Gye Kya🙄🙄",
    "Ek Song Play Kro Na Plss😕",
    "Aap Kaha Se Ho..??🙃",
    "Hello KITTY Bhahbi Ji Namaste😛",
    "Hello DEEP Baby Kkrh..?🤔",
    "Do You Know Who Is My Owner.?",
    "VIKKY BHABHI kaisi hai...🤗",
    "Aur Batao Kaisa Ho Baby😇",
    "Tumhari Mummy Kya Kar Rahi Hai🤭",
    "Laduu meri bhanji ko jante ho🥺🥺",
    "Oye Pagali Online Aa Ja😶",
    "Aaj Holiday Hai Kya School Me..??🤔",
    "Oye Good Morning😜",
    "DEEP Suno Ek Kam Hai Tumse🙂",
    "Koi Song Play Kro Na😪",
    "Nice To Meet Uh☺",
    "Hello 🙊 SUNO ROBIN Kutta hai",
    "Study Complete Hua Doctor Boy??😺",
    "Bolo Na Kuch ANIKET (iit) chhakka🤭",
    "SONALI Kon Hai...??😅",
    "Tumhari Ek Pic Milegi..?😅",
    "Mummy Aa Gyi Kya😆😆😆",
    "Or Batao KITTY Bhabhi Kaisi Hai😉",
    "I Love You DEEP 🙈🙈🙈",
    "Do You Love Me..DEEP?👀",
    "Rakhi Kab Band Rahi Ho.??🙉",
    "Ek Song Sunau..?😹",
    "Online Aa Ja Re Song Suna Rahi Hu😻",
    "Instagram Chalati Hai Cool Angel ..??🙃",
    "Whatsapp Number Doga Apna Tum..?😕",
    "Tumhe Kon Sa Music Sunna Pasand Hai..?🙃",
    "Sara Kam Khatam Ho Gya DEEP..?🙃",
    "Kaha Se Ho Aap😊",
    "Suno Na harshu cute hai n🧐",
    "Mera Ek Kaam Kar Doga..?",
    "By Tata Mat Bat Karna Aaj Ke Bad😠",
    "Mom Dad Kaisa Hain..?❤",
    "Kya Hua kartik (offline) ko nhi jante ho..?👱",
    "Bohot Yaad Aa Rhi Hai Kartik mere bete 🤧❣️",
    "Bhul Gye Mujhe Robin bete 😏😏",
    "Juth Nhi Bolna Chahiye junior 🤐",
    "Kha Lo Bhaw Mat Kro Baat Unknown😒",
    "Kya Hua😮😮 MAURYA CHAKKA 😁",
    "Hii👀",
    "Aapke Jaisa Dost Ho Sath Me Fir Gum Kis Bat Ka 🙈",
    "Aaj Mai Sad Hu ☹️",
    "Mujhse Bhi Bat Kar Lo Na 🥺🥺",
    "Kya Kar RahI MERI DEEP 👀",
    "Kya Hal Chal Hai DEEP Baby🙂",
    "Kaha Se Ho Aap..?🤔",
    "Chatting Kar Lo Na..🥺",
    "Me Masoom Hu Na🥺🥺",
    "Kal Maja Aya Tha Na Satyam baby🤭😅",
    "Junior Group Me Bat Kyu Nahi Karti Hai😕",
    "Aap Relationship Me Ho..?👀",
    "Harshu Kitna Chup Rahte Ho Yrr😼",
    "Aapko Gana Gane Aata Hai..?😸",
    "Ghumne Chalo Chand Par ..??🙈",
    "Ara Jila BRAND Hai n ✌️🤞",
    "Ham Dost Ban Sakte Hai...?🥰",
    "Kuch Bol Kyu Nhi Rahe Ho..🥺🥺",
    "Kuch Members Add Kar Do 🥲",
    "Single Ho Ya Mingle 😉",
    "Aao Party Karte Hain😋🥳",
    "Rahul Motu Bhai kha ho 🧐",
    "Mujhe Bhul Gyi n Pagli 🥺",
    "Yaha Aa Jao:- [ @Learnandshareofficial ] Masti Karenge 🤭🤭",
    "Truth And Dare Kheloge..? 😊",
    "Aaj Mummy Ne Data Yr🥺🥺",
    "Join Kar Lo:- [ @WORLD_ALPHA ] 🤗",
    "Gali sun na hai Do or Die ke pass jao😗😗",
    "Tumhare Dost Kaha Gye🥺",
    "My Cute Owner [ @ll_ALPHA_BABY_lll ]🥰",
    "Kaha Khoye Ho Rupak Sir g😜",
    "Good N8 Ji Bhut Rat Ho gyi🥰",
]

@app.on_message(filters.command(["tagall", "spam", "tagmember", "utag", "stag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("This Command Only For Groups.")

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
        return await message.reply("You Are Not Admin Baby, Only Admins Can Tag Members.")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall Type Like This / Reply Any Message Next Time")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall Type Like This / Reply Any Message Next Time...")
    else:
        return await message.reply("/tagall Type Like This / Reply Any Message Next Time..")
    
    if chat_id in spam_chats:
        return await message.reply("Please At First Stop Running Process...")
    
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    
    try:
        async for usr in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if usr.user.is_bot:
                continue
            usrnum += 1
            usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

            if usrnum == 1:
                if mode == "text_on_cmd":
                    txt = f"{usrtxt} {random.choice(TAGMES)}"
                    await client.send_message(chat_id, txt)
                elif mode == "text_on_reply":
                    await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
                await asyncio.sleep(4)
                usrnum = 0
                usrtxt = ""
    except Exception as e:
        print(f"Error in tagall: {e}")
    finally:
        try:
            spam_chats.remove(chat_id)
        except:
            pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("Currently I'm Not Tagging...")
    
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    
    if not is_admin:
        return await message.reply("You Are Not Admin Baby, Only Admins Can Tag Members.")
    
    try:
        spam_chats.remove(message.chat.id)
    except:
        pass
    return await message.reply("♦ SONALI stopped tagging...♦") 