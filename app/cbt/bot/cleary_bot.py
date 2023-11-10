from discord import Client
from message_handlers.memes import prophet_has_spoken
import logging
from message_handlers import load, __handlers__
import sys


class ClearyBot(Client):
    async def on_ready(self):
        logging.warning(f"Logged on as {self.user}!")
        load()

    # For each message, iterate through the handlers and run them
    async def on_message(self, message):
        logging.warning(f"Message from {message.author}: {message.content}")
        # Retrieve the individual handlers,imports them, and the decorator handles whether or not the actual functions run
        for name, module, func_name in __handlers__:
            handler = getattr(sys.modules[module], func_name)
            await handler(message)
        await prophet_has_spoken(message)
