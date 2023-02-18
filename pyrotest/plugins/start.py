from pyrogram import Client, filters
from pyrogram.types import Message, Chat, User


@Client.on_message(filters.command("start"))
async def request(Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await message.reply_text("HELLO {user_name}")
