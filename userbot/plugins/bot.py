#make by legendx22 
#kang with keep credits

from telethon import events, Button, custom
@tgbot.on(events.InlineQuery)
async def inline_handler(event):
chut = event.builder
butts = [[Button.url("REPO :gift_heart:", "https://github.com/legendx22/LEGEND-BOT"), Button.url('STRING SESSION :zap:', 'http://repl.it/@legendx22/LEGEND-BOT#main.py')]]
query = event.text
me = await borg.get_me()
if query.startswith("repo") and event.query.user_id == me.id:
    legend = chut.article(
                       title="REPO OF LEGEND BOT",
                       text="REPO OF LEGEND BOT + STRING SESSION",
                       buttons=butts,
                   )
    await event.answer([legend])
