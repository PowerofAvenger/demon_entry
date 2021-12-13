from chatrobot.plugins.sql.users_sql import add_me_in_db, his_userid
from chatrobot.plugins.sql.checkuser_sql import add_usersid_in_db, already_added, get_all_users
from telethon import custom, events, Button
import re
from telethon.tl.functions.users import GetFullUserRequest

bot = chatbot
from telethon.tl.types import MessageEntityMentionName


@chatbot_cmd("start", is_args=False)
async def sedlyfsir(event):
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    oknoob = Config.OWNER_ID
    formaster = "**Sir. How Can I Help You?**"
    if event.sender_id == Config.OWNER_ID:
        ok = await chatbot.send_message(event.chat_id, message=formaster, buttons = [
             [custom.Button.inline("Commands For Owner.", data="cmds")],
             [custom.Button.inline("Close 🔐", data="close ")],
              ]
             )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
            await chatbot.send_message(Config.DUMB_CHAT, f"**NEW USER ! \nUser ID :** `{event.chat_id}`\n**")
        elif already_added(event.chat.id):
            pass
        elif not already_added(event.chat.id):
            add_usersid_in_db(event.chat.id)
            await chatbot.send_message(1741502445, f"**#New_Chat\n\nChat ID :** `{event.chat.id}`")
        fekp = [[Button.inline("REGISTER FOR COMMUNITY", data="entryy")]]
        await event.reply(f"**Hello {event.sender.first_name}!\nYou Can regiser for community entry Using This Bot....!\n\nThis Bot Was Created By @dr_strange_6969**", buttons=fekp)
    
        
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def help(event):
    await event.delete()
    
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"entryy")))
async def n(event):
    sed = event.sender.first_name
    k = f"@{event.sender.username}" if event.sender.username else "@IᴅK"
    ne = f"""**

┏Name ⥇ {sed}
┗Username ⥇ {k}

✘  ✘**

"""
    tf = [[Button.inline("Yes.", data="eyes"), Button.inline("No.", data="noen")]]
    n = await event.reply(f"**Ur Entry Will Be Taken Like Below Format Are U Sure...?**\n\n{ne}", buttons=tf)
    await event.delete()
    
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"noen")))
async def n(event):
    await event.delete()
    await event.reply("**Ok Cancelled!!**")
    
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"eyes")))
async def n(event):
    sed = event.sender.first_name
    k = f"@{event.sender.username}" if event.sender.username else "@IᴅK"
    ne = f"""**

┏Name ⥇ {sed}
┗Username ⥇ {k}

✘  ✘**

"""
    await bot.send_message(1703105698, ne)
    na = await event.reply("`Donee... Now please enter your skills`")
    await event.delete()
              
              
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"cmds")))
async def help(event):
    msg = (f"<b><u> Commands </b></u> \n<code>➤ /start - Starts Bot \n➤ /block - Reply To User To Block Him \n➤ /unblock - Unblocks A User \n➤ /alive - Am I Alive? \n➤ /broadcast - Broadcasts A Message \n➤ /stats - Show Bot Stats </code>")
    await event.edit(msg, parse_mode="HTML")
