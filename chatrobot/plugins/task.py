from telethon import events, Button
import re, os
from chatrobot import chatbot as bot

@bot.on(events.NewMessage(pattern="Gib Trick$"))
async def _(event):
   await event.reply("hi")
