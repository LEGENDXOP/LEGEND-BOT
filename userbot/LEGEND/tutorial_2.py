# HELLO VRO
# THIS IS FOR ULTROID
@ultroid_cmd(pattern="tag")
async def hehe (event):
  Legend = await event.get_reply_message()
  X = Legend.sender
  pro = X.first_name
  boy = X.last_name
  await event.edit(f"HELLO BRO THIS IS YOUR ID : {X.id}\n AND THIS IS YOUR USERNAME : {X.username} \n AND THIS IS YOUR NAME : {pro} {boy}")



# FOR Grand official
from LEGEND.events import register
@register(pattern="/taag")
async def hehe (event):
  try:
    legend = await event.get_reply_message()
    x = legend.sender
    pro = x.first_name
    boy = x.last_name
    await event.reply(f"hello bro this is your id : {x.id}\n and this is your username : {x.username} \n and this is your name : {pro} {boy} ")
  except:
    await event.reply("SIR TAG A USER PLEASE ")
