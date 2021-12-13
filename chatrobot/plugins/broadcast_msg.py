from chatrobot.plugins.sql.checkuser_sql import get_all_users

@chatbot_cmd("broadcast", is_args=True)
@god_only
async def sedlyfsir(event):
   bot = chatbot
   async with bot.conversation("MRVIRUS_XD") as conv:
    msgtobroadcast = await conv.send_message("**Ok Now Send Me The Message For Broadcast...!**")
    sed = await conv.get_response()
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            await chatbot.send_message(int(starkcast.chat_id), sed)
        except Exception as e:
            error_count += 1
    sent_count = error_count - len(userstobc)
    await chatbot.send_message(
        "MRVIRUS_XD",
        f"<b>Broadcast Done in <u>{sent_count}</u> Group/Users and I got <u>{error_count}</u> Error and Total Number Was <u>{len(userstobc)}</u></b>",
        parse_mode="HTML"
    )
    await chatbot.send_message(Config.DUMB_CHAT, f"**#Broadcast\n\nYou BroadCasted A New Message.\nSent Count - {sent_count}**")
    await chatbot.send_message(Config.DUMB_CHAT, sed)
