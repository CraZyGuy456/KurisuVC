import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

from pyrogram import Client, idle 

from DaisyXMusic.config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "SatoruPyro",
   api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

app.start()
