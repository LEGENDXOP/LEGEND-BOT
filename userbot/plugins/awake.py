"""Check if userbot awake or not . 

"""
#make by @LEGENDX22 don't kang this plugin
# if you kang then keep credits
#cReDiTs - @ProgrammingError
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, legendversion, StartTime, CMD_HELP
from . import legend
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PHOTTO = Config.ALIVE_PHOTTO
if ALIVE_PHOTTO is None:
  ALIVE_PHOTTO = "https://telegra.ph/file/0e36b02061064b7229e3b.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND BOY"

global ghanti
        
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya 😅           
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   tag = borg.uid
   uptm = await legend.get_readable_time((time.time() - StartTime))
   ALIVE_MESSAGE= " ⚡ LEGEND BOT ⚡  IS ON 🔥 FIRE 🔥 \n\n"
   ALIVE_MESSAGE += "🔱 SYSTEM STATUS🔱\n"
   ALIVE_MESSAGE += "🔱TELETHON VERSION🔱 : 6.0.9\n"
   ALIVE_MESSAGE += "🔱LEGEND VERSION🔱 :   2.5\n"
   ALIVE_MESSAGE += f"🔱UPTIME🔱 : `{uptm}`\n"
   ALIVE_MESSAGE += f"⚜️ MY BOSS ⚜️: [{DEFAULTUSER}](tg://user?id={tag})\n"
   ALIVE_MESSAGE += "⚜️GROUP⚜️ : [SUPPORT](https://t.me/LEGEND_USERBOT_SUPPORT)\n\n"
   ALIVE_MESSAGE += ":⚜️Deploy⚜️ **LEGEND BOT** : [ᖇᏋᎵᏫ](https://github.com/legendx22/LEGEND-BOT)\n"   
   await awake.delete() 
   await borg.send_file(awake.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "awake": "**Plugin : **`awake`\
    \n\n**Syntax : **`.awake`\
    \n**Function : **you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)

