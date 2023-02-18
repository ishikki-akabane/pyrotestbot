import logging
import time

from pyrogram import Client


API_KEY = 
API_HASH = ""
BOT_TOKEN = ""

# enable logging
FORMAT = "[Blue] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("bluelogs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)

LOGGER = logging.getLogger('[Blue]')
