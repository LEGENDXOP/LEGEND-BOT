#credits @LEGENDX22
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

# uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/63e17e3cc1f6ec8fc0cee.mp4"
pm_caption = "**This is LEGEND Userbot**\n\n"

pm_caption += "Hi THERE 👋 MASTER ! I am Alive. All functions are working properly.\n\n"
pm_caption += "⚡️Status⚡️\n\n"
pm_caption += "😎Telethon Version : (1.16.04)\n"
pm_caption += "🥳Python : (3.8.3)\n"
pm_caption += "😮Version : (1.0)\n"
pm_caption += "🥱A.I Verision : Beta **1.0.01** [Ask Support Group Master](t.me/teamishere)\n"
pm_caption += "😱Sudo : (enabled For Master)\n"
pm_caption += "🤫Database status : All Fine👌\n"
pm_caption += f"🥰My Pro Master : {DEFAULTUSER}\n\n"
pm_caption += "🤖[✅ Deploy Me Now ✅](https://github.com/legendx22/LEGEND-BOT)\n\n"
pm_caption += "© [Channel](https://t.me/hackerget0)\n\n"
pm_caption += "    [Join Here](https://t.me/eamishere) For Latest Updates\n\n"
pm_caption += "SYSTEM HEALTH : STABLE 😎👍 "



@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
