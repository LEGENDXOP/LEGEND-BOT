
from userbot import CMD_HELP, bot
from userbot.utils import admin_cmd
from telethon.events import ChatAction
#made by shivam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
from userbot import bot, CMD_HELP
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from userbot.utils import register
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
from userbot import TEMP_DOWNLOAD_DIRECTORY
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
import   os,re, bs4, requests, io
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from telethon import events
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from pathlib import Path
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam
from os import remove
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
from bs4 import BeautifulSoup
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from re import findall
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
from urllib.parse import quote_plus
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from requests import get
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from PIL import Image
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from telethon.tl.types import MessageMediaPhoto
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
import urllib
from userbot import bot as borg
import os
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from bs4 import BeautifulSoup
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
opener = urllib.request.build_opener() ; useragent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36' ; opener.addheaders = [('User-agent', useragent)]
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
from userbot.legend import MASTER
LEGENDX = MASTER
WAFU_CHATID=int(os.environ.get("WAFU_CHATID",-1001230114424))
async def ParseSauce(googleurl):   
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, 'html.parser')
    results = {'similar_images': '', 'best_guess': ''}
    try:
        for similar_image in soup.findAll('input', {'class': 'gLFyf'}):
            url = 'https://www.google.com/search?tbm=isch&q=' + \
                urllib.parse.quote_plus(similar_image.get('value'))
            results['similar_images'] = url
    except BaseException:
        pass
    for best_guess in soup.findAll('div', attrs={'class': 'r5a77d'}):
        results['best_guess'] = best_guess.get_text()
    return results
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
async def scam(results, lim):
    single = opener.open(results['similar_images']).read()
    decoded = single.decode('utf-8')
    imglinks = []
    counter = 0
    pattern = r'^,\[\"(.*[!png|!jpg|!jpeg])\",[0-9]+,[0-9]+\]$'
    oboi = re.findall(pattern, decoded, re.I | re.M)
    for imglink in oboi:
        counter += 1
        if not counter >= int(lim):
            imglinks.append(imglink)
        else:
            break
    return imglinks
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
async def chrome(chrome_options=None):
    if chrome_options is None:
        chrome_options = await options()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.mkdir(TEMP_DOWNLOAD_DIRECTORY)
    prefs = {'download.default_directory': TEMP_DOWNLOAD_DIRECTORY}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    return driver
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
#Made by Shivam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam

@bot.on(events.NewMessage(incoming=True))
async def on_new_message(event):
		


        name = event.raw_text
        snip = """appeared!
Add them to your harem by sending /protecc character name""" 


        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
				
                      
                      photo = io.BytesIO()
                      await event.client.download_media(event.media, photo)
                      image = Image.open(photo)
                      name = "okgoogle.png"
                      image.save(name, "PNG")
                      image.close()
                      searchUrl = 'https://www.google.com/searchbyimage/upload'
                      multipart = {
                              'encoded_image': (name, open(name, 'rb')),
                              'image_content': ''
                      }
                      response = requests.post(searchUrl,
                                                                       files=multipart,
                                                                       allow_redirects=False)
                      fetchUrl = response.headers['Location']
                      match = await ParseSauce(fetchUrl +"&preferences?hl=en&fg=1#languages")
                      guess = match['best_guess']
                      guesss = guess[12:]
                      #Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
                      #Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
                      #Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
                      #Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam
                      try:
                            from userbot.modules.sql_helper.autowafu_sql import get_current_wafu_settings
                            from userbot.modules.sql_helper.autowafu_sql import update_previous_wafu
                      except AttributeError:
                            return
                      cws = get_current_wafu_settings(event.chat_id)
                      if cws:
                          await event.reply( f"/protecc {guesss}")
                      else:
                          await borg.send_message( WAFU_CHATID,f"/protecc {guesss}")
            except Exception as e:
                pass
#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made by Sh1vam#Made#Made by Shivam
#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam#Made by Shivam

'''@bot.on(ChatAction)
async def wafu_to_chat(event):
    try:
        from userbot.plugins.sql_helper.autowaifu_sql import get_current_wafu_settings
        from userbot.plugins.sql_helper.autowaifu_sql import update_previous_wafu
    except AttributeError:
        return
    cws = get_current_wafu_settings(event.chat_id)
    if cws:'''



@register(outgoing=True, pattern=r"^.savewaifu(?: |$)(.*)")
async def save_wafu(event):
    try:
        from userbot.plugins.sql_helper.autowaifu_sql import add_wafu_setting
    except AttributeError:
        return await event.edit("`Running on Non-SQL mode!`")

    
    string = """appeared!
Add them to your harem by sending /protecc character name"""
    msg_id = None
    if add_wafu_setting(event.chat_id, 0,string, msg_id) is True:
        await event.edit('Auto wafu mode on')
    else:
        await event.edit(f"`{LEGENDX}`: **auto wafu already present**")






@register(outgoing=True, pattern="^.checkwaifu$")
async def show_wafu(event):
    try:
        from userbot.plugins.sql_helper.autowaifu_sql import get_current_wafu_settings
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    cws = get_current_wafu_settings(event.chat_id)
    if not cws:
        await event.edit(f"`{LEGENDX}`: **auto wafu not on.**")
        return
    else:
        await event.edit(f"`{LEGENDX}`: **auto wafu on.**")




@register(outgoing=True, pattern="^.clearwaifu$")
async def del_wafu(event):
    try:
        from userbot.plugins.sql_helper.autowaifu_sql import rm_wafu_setting
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    if rm_wafu_setting(event.chat_id) is True:
        await event.edit(f"`{LEGENDX}`: **auto wafu stops**")
    else:
        await event.edit(f"`{LEGENDX}`: ** no auto wafu on. **")

