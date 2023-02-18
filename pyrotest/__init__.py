import logging
import time

from pyrogram import Client


API_KEY = 123456789
API_HASH = ""
BOT_TOKEN = ""
DOWNLOAD_DIRECTORY = "./"

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
