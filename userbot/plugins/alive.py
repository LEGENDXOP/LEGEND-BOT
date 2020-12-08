import asyncio
from telethon import events
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/93f85e88789464793bc5c.jpg"
pm_caption = "__**🔥🔥LEGEND BOT IS ON FIRE🔥🔥**__\n\n"

pm_caption += f"               _MY MASTER__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😏LEGEND BOT😏       : __**{1.2.2**__\n"

pm_caption += f"😤Sudo😤            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/hackerget0)\n"

pm_caption += "😱OWNER😱    : [Nub Here](https://t.me/LEGENDX22)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/legendx22/LEGEND-BOT) 🤐  [LICENSE](https://github.com/legendx22/LEGEND-BOG/blob/master/LICENSE)"

pm_caption += " 😡Haters apni GA** maraao😡\n\n"

@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):


    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
