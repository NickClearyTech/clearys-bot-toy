from message_handlers import message_handler
from discord.message import Message
import functools
import logging


# A bot handler to reply with "THE PROPHET HAS SPOKEN" whenever richard mentions emacs in the emacs channel
@message_handler(channel=992166504269357146, user=192024972644974592)
async def prophet_has_spoken(message: Message):
    if "emacs" in message.content.lower():
        await message.reply("*THE PROPHET HAS SPOKEN*")
