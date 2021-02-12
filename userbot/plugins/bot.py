# make by @LEGENDX22
# inline alive
# modify by proboy22
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from userbot import bot as borg
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = borg.uid

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND BOY"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

pro_text=(f"**LEGEND BOT IS ON FIRE **\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n🔥 About My System 🔥\n\n➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.17.5\n➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/hackerget0)\n➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [LEGEND BOT](https://github.com/legendx22)\n➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [LEGEND-BOT](https://github.com/legendx22/LEGEND-BOT)\n\n➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ok})\n")
TG_BOT_USER_NAME_BF_HER = os.environ.get("ALIVE_PHOTTO", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/legendx22/LEGEND-BOT"),
                    Button.url("Deploy", "https://heroku.com/deploy?template=https://github.com/legendx22/LEGEND-BOT/blob/master")],
                    [Button.url("String", "https://repl.it/legendx22/LEGEND-BOT#main.py"),
                    Button.url("Channel", "https://t.me/hackerget0"),
                ]
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="LEGEND BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="LEGEND BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)
