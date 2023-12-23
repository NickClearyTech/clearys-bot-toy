import random

from discord import Status, CustomActivity
from discord.ext.commands import Bot
import logging

from message_handlers import __handlers__
from utils import bot_activities
import sys


class ClearyBot(Bot):
    async def on_ready(self):
        logging.warning(f"Logged on as {self.user}!")
        logging.warning(f"Loaded {len(__handlers__)} handlers")
        await self.change_presence(
            status=Status.online,
            activity=CustomActivity(name=random.choice(bot_activities.bot_activites)),
        )

    # For each message, iterate through the handlers and run them

    async def on_message(self, message):
        logging.warning(f"Message from {message.author}: {message.content}")
        # If bot, we don't care, return
        if message.author.bot:
            return
        # Process any commands that are valid here
        await self.process_commands(message)
        # Retrieve the individual handlers,imports them, and the decorator handles whether the actual functions run
        for _, module, func_name in __handlers__:
            handler = getattr(sys.modules[module], func_name)
            await handler(message)
