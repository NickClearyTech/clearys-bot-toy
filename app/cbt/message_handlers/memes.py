import random

from message_handlers import message_handler
from discord.message import Message
from message_handlers import handler
import logging

emacs_quotes_options = [
    "eMaCS Is THe BEsT tExt edIToR",
    "Have you considered trying nvim?",
    "FYI: package update 1.69 is now available for Deldo. Resolves numerous bugs with the Thurstmaster series' integration",
    "emacs? Is that like an off brand iMac?",
    "*spends 80 hours a week configuring text editor*",
    "Dror ragzlin... dror ragzlin... had a warrior's heart. And a killer emacs config.",
]


# A bot handler to reply with "THE PROPHET HAS SPOKEN" whenever richard mentions emacs in the emacs channel
@handler(
    name="prophet has spoken", channels=[992166504269357146], users=[192024972644974592]
)
async def prophet_has_spoken(message: Message):
    if "emacs" in message.content.lower():
        await message.reply("*THE PROPHET HAS SPOKEN*")


@handler(name="Emacs quotes", users=[192024972644974592])
async def emacs_quotes(message: Message):
    if "emacs" in message.content.lower() and random.randint(1, 10) > 4:
        await message.reply(random.choice(emacs_quotes_options))
