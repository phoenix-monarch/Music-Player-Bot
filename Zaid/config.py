##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001688479760'))
ASS_ID = int(getenv("ASS_ID"))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
RESULT_PIC = getenv('RESULT_PIC', "https://telegra.ph/file/62c6a23532aed6f4def02.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://telegra.ph/file/cf12b3276d8b2f1aefe48.jpg")
PING_IMG = getenv('PING_IMG', "https://telegra.ph/file/cfb574159bff272493570.jpg")
AUTO_LEAVE_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_LEAVE = getenv('AUTO_LEAVING_ASSISTANT', None)
