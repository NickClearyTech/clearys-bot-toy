from discord import Client
from message_handlers.memes import prophet_has_spoken
import logging
from message_handlers import load, __handlers__
import sys


class ClearyBot(Client):
    async def on_ready(self):
        logging.info(f"Logged on as {self.user}!")
        load()

    async def on_message(self, message):
        logging.warning(f"Message from {message.author}: {message.content}")
        for name, module, func_name in __handlers__:
            thing = getattr(sys.modules[module], func_name)
            await thing(message)
            logging.warning(module)
        await prophet_has_spoken(message)
