import os
from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.utils import load_module, start_assistant
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils

sed = logging.getLogger("userbot")


LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
    

import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print("➠ The most Powerful LegendBOT is on fire 🔥. Check .alive to test that bot is functioning or not . Join http://t.me/teamishere for any assistance 👀")


if LOAD_ASSISTANT == True:
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
else:
    print("Assitant is Not Loading As U Have Disabled")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()


