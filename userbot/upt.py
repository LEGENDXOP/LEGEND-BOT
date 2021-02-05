import time
import datetime
from . import legend
async def uptm():
   uptm = await legend.get_readable_time((time.time() - StartTime))
