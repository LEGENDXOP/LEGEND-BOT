from userbot.utils import admin_cmd as a
#sleep how many times after each edit in 'lol' 
EDIT_SLEEP = 1
#edit how many times in 'lol' 
EDIT_TIMES = 19


lol_ani = [ 
            "WOW AB BOHOT MAJA AANE WALA HAI TO READY HO ZAO",
            "1..",
            "2...",
            "3....",
            " 𝙰𝙽𝙳 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ", 
            " ✰ *𝚆𝙰𝙰𝙷* ✰     [ㅤ](https://telegra.ph/file/a19b0bf4760fca85bd961.png) ",
            " ✰ *𝙻𝙾𝙻* ✰      [ㅤ](https://telegra.ph/file/ed23819c84bab66e7d92f.png) ",
            " ✰ *𝙴𝙻𝙴𝙲𝚃𝚁𝙸𝙲 𝙱𝙸𝙻𝙻 𝙺𝙾𝙽 𝙱𝙷𝙰𝚁𝙴𝙶𝙰* ✰  [ㅤ](https://telegra.ph/file/53c85b5b354212496746f.png) ",
            " ✰ *𝙹𝙷𝙸𝙽𝙶𝙰 𝙻𝙰𝙻𝙰* ✰    [ㅤ](https://telegra.ph/file/1379a8c9ea40eaa463fd8.png) ",
            " ✰ *𝙽𝙸𝙽𝙹𝙰 𝚃𝙴𝙲𝙷𝙽𝙸𝚀𝚄𝙴* ✰    [ㅤ](https://telegra.ph/file/891a05f03399fb48f40f3.png) ",
            " ✰ *𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝙲𝙷𝙾𝚁* ✰    [ㅤ](https://telegra.ph/file/542a1f433c263e4f3f984.png)",
            " ✰ *𝚂𝙰𝙰𝚁 𝙳𝙰𝚁𝙳* ✰    [ㅤ](https://telegra.ph/file/bfa114bbd4b2044cf5933.png)",
            " ✰ *𝚂𝚆𝙰𝙳 𝙰𝙰𝚈𝙰* ✰    [ㅤ](https://telegra.ph/file/3830d44f9333e3c21b2cd.png)",
            " ✰ *𝙺𝙰𝙰𝙼 𝚃𝙰𝙼𝙰𝙼* ✰    [ㅤ](https://telegra.ph/file/ececebb55e5f29be0afcf.png)",
            " ✰ *𝙹𝙰𝙻𝙴𝙱𝙸 𝙺𝙷𝙰𝚈𝙸* ✰    [ㅤ](https://telegra.ph/file/389a857af3bf833d3ccb2.png)",
            " ✰ *𝙼𝙾𝚅𝙴 𝙾𝚄𝚃* ✰    [ㅤ](https://telegra.ph/file/2a30a5514b022120a82b9.png)",
           
            " ✰ *𝚂𝚄𝙳𝙷𝙰𝚁 𝙹𝙰* ✰    [ㅤ](https://telegra.ph/file/c5cd50018e304056484f2.png)",
            " ✰ *𝙳𝙾𝙽𝚃 𝙳𝙾 𝙼𝙰𝚂𝚃𝙸* ✰    [ㅤ](https://telegra.ph/file/455b959424b17f9fb570e.png)",
            " ✰ *𝙲𝙷𝙰𝙿𝙿𝙰𝙻 𝚆𝙰𝚁* ✰    [ㅤ](https://telegra.ph/file/a0fad91da8b4556c67a2d.png)"
]
@borg.on(a(pattern=r"hehe"))
async def LEGENDX (event):
  msg = await event.edit('DEKHNA AAB MAJA AAEGA 😂')
    for x in range(EDIT_TIMES):
        msg.edit_text(lol_ani[x%19],parse_mode='markdown')
        time.sleep(5)
    msg.edit_text('*MAJA AAYA KYA 😄*[ㅤ](https://telegra.ph/file/381dd2ea242e0bd292434.png) *AGAR HA THEN MAKE* [𝙻𝙴𝙶𝙴𝙽𝙳 𝚄𝚂𝙴𝚁𝙱𝙾𝚃](t.me/teamishere)  ',parse_mode='markdown')
