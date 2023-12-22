from discord.ext.commands import Bot
import logging
from message_handlers import load, __handlers__
import sys


class ClearyBot(Bot):

    async def on_ready(self):
        logging.warning(f"Logged on as {self.user}!")
        load()
        logging.warning(f"Loaded {len(__handlers__)} handlers")

    # For each message, iterate through the handlers and run them
    async def on_message(self, message):
        logging.warning(f"Message from {message.author}: {message.content}")
        # If bot, we don't care, return
        if message.author.bot: return
        # Process any commands that are valid here
        await self.process_commands(message)
        # Retrieve the individual handlers,imports them, and the decorator handles whether or not the actual functions run
        for name, module, func_name in __handlers__:
            handler = getattr(sys.modules[module], func_name)
            await handler(message)
