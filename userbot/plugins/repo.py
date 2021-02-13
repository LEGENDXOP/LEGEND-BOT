# MADE BY LEGENDX22
# IDEA BY PROBOY22
# CREDITS TEAMLEGEND
# PLEASE KEEP CREDITS 🥺



from telethon import events, Button, custom
from userbot.legend import BOT

@tgbot.on(events.InlineQuery)
async def inline_handler(event):
 LEGEND = event.builder
 X= [[Button.url(f"⚜️ {BOT} REPO ⚜️", "https://github.com/LEGENDXOP/LEGEND-BOT"),Button.url("🔥SUPPORT 🔥", "https://t.me/LEGEND_USERBOT_SUPPORT")]]
 query = event.text
 me = await borg.get_me()
 if query.startswith("repo") and event.query.user_id == me.id:
  PROBOY = LEGEND.article(
                           title=f"{BOT} REPO",
                           text=f"{BOT} REPO AND GROUP LINK",
                      buttons=X,
               )
  await event.answer([PROBOY])
 else:
  return
