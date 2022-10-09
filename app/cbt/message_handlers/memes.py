from message_handlers import message_handler
from discord.message import Message
import functools
import logging


# A bot handler to reply with "THE PROPHET HAS SPOKEN" whenever richard mentions emacs in the emacs channel
@message_handler(channel=725357726133125223, user=475488656170156039)
async def prophet_has_spoken(message: Message):
    if "emacs" in message.content.lower():
        await message.reply("*THE PROPHET HAS SPOKEN*")
