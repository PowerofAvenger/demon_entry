from chatrobot.plugins.sql.checkuser_sql import get_all_users
import io

@chatbot_cmd("stats", is_args=False)
@god_only
async def starkisnoob(event):
    starkisnoob = get_all_users()
    await event.reply(f"<b>I have <u>{len(starkisnoob)}</u> Users In Database.</b>", parse_mode="HTML")

@chatbot_cmd("alive", is_args=False)
@god_only
async def stark(event):
    await event.reply("<b><u>Yeah, I am Alive.</b></u>", parse_mode="HTML")

@chatbot_cmd("repo", is_args=False)
async def stark(event):
    await event.reply("<b><u>My Repo is Here :</b></u> <code>https://github.com/infotechbro/ChatBot1</code>", parse_mode="HTML")
    
@chatbot_cmd("users", is_args=False)
@god_only
async def starkisnoob(event):
    starkisnoob = get_all_users()
    sed = "Lɪsᴛ Oғ Tᴏᴛᴀʟ Usᴇʀs Iɴ Bᴏᴛ. \n\n"
    for x in starkisnoob:
        ehh = int(x.chat_id)
        sed += (f"➥ [{ehh}](tg://user?id={ehh}) \n")
        await event.reply(sed)
