#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27759631
API_HASH = b105a36e67eb89caade6ad2fcc3e9a2f
BOT_TOKEN = 6630718813:AAHIM6R9QDs-0sHvgIUlPrtTR83w7I83yQ0
SESSION = BQE9p8oAhjePmKQdhvr2-jMF52AJBeC3AiLTe8ZazVBGUaxUbAXV4OIxI5l65FNK0xATqA-5876nY1yYVfgRz_dCJ5oxg5MBUyZG3ltGE647NSPs6o8YIrDxiT52mbbxfd_hQlUv-SZ0vEbBAr9wBabbQfAMjfBvF97BEx_ekeeMoLy7xo5E5TssQYmw51j8I0k0mArQChShqAszg-6CZxbaObxDG_Hszbt7YVTEHZzcSatGkF8lVSvWGFOKe59eQmv1vtVBnaA0VrjIkNUBLkUL9gHEFSuzOaalTHXI674FzZ-7nRy3No91l1JPIq2eEpkaamhl9cXxUDZeNxJwJi6RslzYGgAAAAEwXsrnAA
FORCESUB = jaatbots
AUTH = 5106485991

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
