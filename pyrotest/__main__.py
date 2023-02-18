from pyrogram import Client
from pytgcalls import idle
import os
from pyrotest import API_ID, API_HASH, BOT_TOKEN, DOWNLOAD_DIRECTORY, LOGGER
import asyncio

async def load_start():
    LOGGER.info("[INFO]: STARTED")
    
    
Client(
    name="pyrotest",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=min(32, os.cpu_count() + 4),
    workdir=DOWNLOAD_DIRECTORY,
    sleep_threshold=60,
    in_memory=True,
    plugins={"root": "pyrotest.plugins"},
).start()


loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())


idle()
loop.close()
