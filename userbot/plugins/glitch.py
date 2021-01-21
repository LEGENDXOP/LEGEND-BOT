"""
designed By @Krishna_Singhal in userge
ported to telethon by @mrconfused and @sandy1709
"""
import asyncio
import shlex
from PIL import Image 
from userbot import LOGS , CMD_HELP
from telethon import functions, types
from userbot.utils import admin_cmd
from glitch_this import ImageGlitcher
from typing import Optional, Tuple


from userbot import bot, CMD_HELP, LOGS
from userbot.events import register

async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    print(
        "[[[Extracting a frame from %s ||| Video duration => %s]]]",
        video_file,
        duration,
    )
    ttl = duration // 2
    thumb_image_path = path or os.path.join("./temp/", f"{basename(video_file)}.jpg")
    command = f"ffmpeg -ss {ttl} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        print(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


@register(pattern="^.(glitch|glitchs)(?: |$)(.*)", outgoing=True)
async def glitch(event):
    await event.edit("```Glitching Wait...```")
    cmd = event.pattern_match.group(1)
    input = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await event.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    reply_to_id = event.reply_to_msg_id
    remixsticker = await reply.download_media(file="./temp/")
    if not remixsticker.endswith(('.mp4', '.webp', '.tgs', '.png', '.jpg')):
        os.remove(remixsticker)
        await event.edit("`Media not found...`")
        return
    file = os.path.join("./temp/", "glitch.png")
    if input:
        if not input.isdigit():
            await event.edit("`You input is invalid, check help`")
            return
        input = int(input)
        if not 0 < input < 9:
            await event.edit("`Invalid Range...`")
            return
    else:
        input = 2
    if remixsticker.endswith(".tgs"):
        file = os.path.join("./temp/", "glitch.png")
        cmd = f"lottie_convert.py --frame 0 -if lottie -of png {remixsticker} {file}"
        stdout, stderr = (await runcmd(cmd))[:2]
        if not os.path.lexists(file):
            await event.edit("`remixsticker not found...`")
            LOGS.info(stdout + stderr)
        glitch_file = file
    elif remixsticker.endswith(".webp"):
        file = os.path.join("./temp/", "glitch.png")
        os.rename(remixsticker, file)
        if not os.path.lexists(file):
            await event.edit("`remixsticker not found... `")
            return
        glitch_file = file
    elif remixsticker.endswith(".mp4"):
        file = os.path.join("./temp/", "glitch.png")
        await take_screen_shot(remixsticker, 0, file)
        if not os.path.lexists(file):
            await event.edit("```remixsticker not found...```")
            return
        glitch_file = file
    else:
        glitch_file = remixsticker
    glitcher = ImageGlitcher()
    img = Image.open(glitch_file)
    if cmd == "glitchs":
        glitched = "./temp/" + "glitched.webp"
        glitch_img = glitcher.glitch_image(img, input, color_offset=True)
        glitch_img.save(glitched)
        await bot.send_file(
            event.chat_id,
            glitched,
            reply_to_message_id=reply_to_id)
        os.remove(glitched)
        await event.delete()
    elif cmd == "glitch":
        Glitched = "./temp/" + "glitch.gif"
        glitch_img = glitcher.glitch_image(
            img, input, color_offset=True, gif=True)
        DURATION = 200
        LOOP = 0
        glitch_img[0].save(
            Glitched,
            format='GIF',
            append_images=glitch_img[1:],
            save_all=True,
            duration=DURATION,
            loop=LOOP)
        await bot.send_file(
            event.chat_id,
            Glitched,
            reply_to_message_id=reply_to_id)
        os.remove(Glitched)
        await event.delete()
    for files in (remixsticker, glitch_file):
        if files and os.path.exists(files):
            os.remove(files)

CMD_HELP.update({
    "glitch":
    ".glitch` reply to media file\
\nUsage:glitches the given mediafile(gif , stickers , image, videos) to a gif and glitch range is from 1 to 8.\
If nothing is mentioned then by default it is 2\
\n\n.glitchs reply to media file\
\nUsage:glitches the given mediafile(gif , stickers , image, videos) to a sticker and glitch range is from 1 to 8.\
If nothing is mentioned then by default it is 2."
})
