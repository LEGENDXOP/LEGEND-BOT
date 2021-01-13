"""Check if userbot awake or not . 

"""
#make by @LEGENDX22 don't kang this plugin
# if you kang then keep credits
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP, StartTime
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

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
    
uptime = get_readable_time((time.time() - StartTime))

ALIVE_MESSAGE= " ⚡ LEGEND BOT ⚡  IS ON 🔥 FIRE ⚜️ \n\n"
ALIVE_MESSAGE += "🔱 SYSTEM STATUS🔱\n"
ALIVE_MESSAGE += "🔱TELETHON VERSION🔱 : 6.0.9\n ⭕ Python: 3.7.4\n"
ALIVE_MESSAGE += "🔱DATABASE STATUS🔱 : Functional\n"
ALIVE_MESSAGE += "🔱Current Branch🔱 : Master\n"
ALIVE_MESSAGE += "🔱LEGEND OS🔱 :   2.0.2\n"
ALIVE_MESSAGE += "🔱WORKING TIME🔱 : {uptime}\n"
ALIVE_MESSAGE += f"⚜️ MY BOSS ⚜️: {DEFAULTUSER} \n"
ALIVE_MESSAGE += "⚜️MADE BY⚜️ 😎 : [LEGEND X](https://t.me/legendx22)\n\n"
ALIVE_MESSAGE += ":⚜️Deploy⚜️ **LEGEND BOT** : [ᖇᏋᎵᏫ](https://github.com/legendx22/LEGEND-BOT)\n"           
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya 😅           
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   await awake.delete() 
   await borg.send_file(awake.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "awake": "**Plugin : **`awake`\
    \n\n**Syntax : **`.awake`\
    \n**Function : **you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)

