# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from decouple import config
from dotenv import load_dotenv, find_dotenv
from . import *


load_dotenv(find_dotenv())

ENV = config("ENV", default=False, cast=bool)


class Var(object):
    # Mandatory
    API_ID = config("API_ID", default=None, cast=int)
    API_HASH = config("API_HASH", default=None)
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    BOT_USERNAME = config("BOT_USERNAME", default=None)
    SUDO = config("SUDO", default=True, cast=bool)
    ADDONS = config("ADDONS", default=False, cast=bool)
    SESSION = config("SESSION", default=None)
    DB_URI = config("DATABASE_URL", default=None)
    HNDLR = config("HNDLR", default=".")
    LOG_CHANNEL = config("LOG_CHANNEL", default=None, cast=int)
    BLACKLIST_CHAT = set(int(x) for x in config("BLACKLIST_CHAT", "").split())
    # heroku stuff
    try:
        HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
        HEROKU_API = config("HEROKU_API", default=None)
    except BaseException:
        HEROKU_APP_NAME = None
        HEROKU_API = None
    # REDIS
    REDIS_URI = config("REDIS_URI", default=None)
    REDIS_PASSWORD = config("REDIS_PASSWORD", default=None)
    MSG_FRWD = config("MSG_FRWD", default=False, cast=bool)
    # SECURITY
    I_DEV = config("I_DEV", default=True)
    # Gdrive
    GDRIVE_TOKEN = config("GDRIVE_TOKEN", default=None)
    GDRIVE_CLIENT_ID = config("GDRIVE_CLIENT_ID", default=None)
    GDRIVE_CLIENT_SECRET = config("GDRIVE_CLIENT_SECRET", default=None)
    GDRIVE_FOLDER_ID = config("GDRIVE_FOLDER_ID", default=None)
    # External Plugins
    PLUGIN_CHANNEL = config("PLUGIN_CHANNEL", default=None)
