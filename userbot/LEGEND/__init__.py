
#Thanks Friday bot
#credits all credits is Friday bot🥰
#ported by LEGENDX22
async def fetch_feds(event, borg):
    fedList = []
    await event.edit("`Fetching Your FeD List`, This May Take A While.")
    reply_s = await event.get_reply_message()
    if reply_s and reply_s.media:
        downloaded_file_name = await borg.download_media(reply_s.media, "fedlist.txt")
        await asyncio.sleep(1)
        file = open(downloaded_file_name, "r")
        lines = file.readlines()
        for line in lines:
            try:
                fedList.append(line[:36])
            except:
                pass
                # CleanUp
        os.remove(downloaded_file_name)
        return fedList
    async with borg.conversation("@MissRose_bot") as bot_conv:
        await bot_conv.send_message("/start")
        await bot_conv.send_message("/myfeds")
        response = await bot_conv.get_response(timeout=300)
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("`Try again after 5 mins.`")
            return
        elif "make a file" in response.text:
            await event.edit(
                "`Boss, You Real Peru. You Are Admin in So Many Feds. WoW!`"
            )
            await response.click(0)
            fedfile = await bot_conv.get_response()
            await asyncio.sleep(2)
            if "You can only use fed commands once every 5 minutes" in fedfile.text:
                await event.edit("`Try again after 5 mins.`")
                return
            if fedfile.media:
                downloaded_file_name = await borg.download_media(fedfile.media, "fedlist.txt")
                await asyncio.sleep(1)
                file = open(downloaded_file_name, "r")
                lines = file.readlines()
                for line in lines:
                    try:
                        fedList.append(line[:36])
                    except BaseException:
                        pass
                os.remove(downloaded_file_name)
        else:
            In = False
            tempFedId = ""
            for x in response.text:
                if x == "`":
                    if In:
                        In = False
                        fedList.append(tempFedId)
                        tempFedId = ""
                    else:
                        In = True

                elif In:
                    tempFedId += x
    await event.edit("`FeD List Fetched SucessFully.`")
    return fedList


async def get_imdb_id(search, event):
    link = "https://yts-subs.com/search/ajax?mov=" + search
    lol = requests.get(link)
    warner_bros = lol.json()
    if warner_bros == []:
        await event.edit("`No Results Found.`")
        warner_media = None
        warner_s = None
    else:
        warner_media = warner_bros[0]["mv_mainTitle"]
        warner_s = warner_bros[0]["mv_imdbCode"]
    return warner_media, warner_s

