import time
import datetime
from . import legend
async def uptm(event):
   uptm = await legend.get_readable_time((time.time() - StartTime))
