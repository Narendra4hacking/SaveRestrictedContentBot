#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24227540
API_HASH = d280dbf1fadbad60856759b39f4091c1
BOT_TOKEN = 6937016968:AAFHpXQR6yJxe4CQaYsb-2YCll7-EQUIEuU
SESSION = BQBISO76jls99LzLbmmaJPiTURPZjaaOVRYLavmz-KcHaNj-EXKD5GgCCSVLiyy3sw4btIEpvp4tFYgugIqTGSpJQic9dR8MST79i94egWNEzizAFI4GB2hNIYrr_glgUYpRrsJkla1dnlV2m5oOFIfVP3YGTSknMRjgWwk1BUA-m0QybkkDjrew7wcqu2vUO4ePzoM7nuDSxUCp7CtNGV8-pM1-i3sG-y4C50bnDQ3hFM77fudlW8QhYQgm__IQ2gUgNTw4DDSceP4Ix7K1I1N-HW36_ynuLkiRkVxKy9WPDtfxzlQX-AalqqnNK0saj4pnrPJ9mMLBb-tEBkZCcZ4AVNHeKgA
FORCESUB = balkarisms
AUTH = 1423040042

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
