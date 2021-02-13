# MAKE BY LEGENDX22
# credits PROBOY22 AND TEAMLEGEND
from telethon import events
import asyncio
#from userbot.utils import admin_cmd
from userbot.events import register 
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os


@borg.on(admin_cmd(pattern=r"hunt"))
async def WooMai(netase):
    if netase.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@hexamonbot"
    link = f"/hunt {song}"
    await netase.edit("```Hunting PokemOne```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await netase.edit("`Catching Weit`")
          try:
              msg = await conv.send_message(link)
              response =  conv.get_response(1)
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await netase.edit("```Please unblock @hexamonbot and try again```")
              return
          await netase.edit("`Pika Pika!😎`")
          await asyncio.sleep(3)
          await bot.send_file(netase.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await netase.delete()



CMD_HELP.update({
    "hexa":"this plugin is made by @legendx22 this plugin is now working properly and this  is op plugin for poke lovers use .hunt"})
