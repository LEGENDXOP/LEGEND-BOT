from telethon import *
#made by Sh1vam Donot kang
#made by Sh1vam Donot kang
#made by Sh1vam Donot kang
from re import findall
#made by Sh1vam Donot kang
#made by Sh1vam Donot kang
#made by Sh1vam Donot kang
from urllib.parse import quote_plus
from urllib.error import HTTPError
#made by Sh1vam Donot kang
from search_engine_parser import GoogleSearch
#made by Sh1vam Donot kang
import urllib
#made by Sh1vam Donot kang
#made by Sh1vam Donot kang
from telethon import events
#made by Sh1vam Donot kang
import asyncio
#made by Sh1vam Donot kang
from userbot.utils import admin_cmd
from userbot import bot as tgbot
from userbot import bot as borg
import os
import re
import urllib
from math import ceil
#made by Sh1vam Donot kang
import requests
from telethon import Button, custom, events, functions
#made by Sh1vam Donot kang
opener = urllib.request.build_opener() ; useragent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36' ; opener.addheaders = [('User-agent', useragent)]
#made by Sh1vam Donot kang#made by Sh1vam Donot kang
#made by Sh1vam Donot kang
#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang
 #made by Sh1vam Donot kang
  #made by Sh1vam Donot kang
#made by Sh1vam Donot kang
#made by Sh1vam Donot kang
@tgbot.on(events.InlineQuery(pattern=r"google (.*)"))
async def inline_id_handler(q_event: events.InlineQuery.Event):
    builder = q_event.builder
    #match = q_event.pattern_match.group(1)

    match,shivam = q_event.pattern_match.group(1).split(";")
    if q_event.query.user_id == bot.uid:
        miraculous = []
        page = findall(r"page=\d+", match)
        try:
            page = page[0]
            page = page.replace("page=", "")
            match = match.replace("page=" + page[0], "")
        except IndexError:
            page = 1
        search_args = (str(match), int(page))
        gsearch = GoogleSearch()
        gresults = await gsearch.async_search(*search_args)
        #msg = ""
        for i in range(int(shivam)):
            try:
                title = gresults["titles"][i]
                link = gresults["links"][i]
                desc = gresults["descriptions"][i]
                #msg += f"[{title}]({link})\n`{desc}`\n\n"
                msg = f"[{title}]({link})\n`{desc}`\n\n"
            except IndexError:
                break
            miraculous.append(
                await q_event.builder.article(
                    title=title,
                    description=desc,
                    text=msg,
                    buttons=Button.switch_inline("Search Again", query="google ", same_peer=True)))
        await q_event.answer(miraculous)
    if not q_event.query.user_id == bot.uid:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/legendx22/LEGEND-BOT ",buttons=[[Button.switch_inline("Search Again", query="google ", same_peer=True)],], )
        await q_event.answer([resultm])
        return
#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang
#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang#made by Sh1vam Donot kang
