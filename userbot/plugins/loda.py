import asyncio
from datetime import datetime

from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND USER"


@borg.on(admin_cmd(pattern="loda$"))
@borg.on(sudo_cmd(pattern="loda$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    ghanta = borg.uid
    event = await edit_or_reply(event, "__**(★ Lessun!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"__**✦҈͜͡➳ Lessun!__**\n★ immunity {ms}\n★ __**Mere**__ **Master ke pass abhi bht immunity h kisi ko bhi chod skte h check krna h kya ** [{DEFAULTUSER}](tg://user?id={ghanta})"
    )


CMD_HELP.update(
    {
    \n\n📌** CMD ★** `.cmd`\
    \n**USAGE   ★  **usage"
    }
)
