from userbot import bot
from userbot.utils import admin_cmd

@bot.on(admin_cmd(pattern=r"space"))
async def space(e):
    await e.edit("ㅤㅤㅤㅤㅤㅤ")