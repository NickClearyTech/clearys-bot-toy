from discord import Client
from message_handlers.memes import prophet_has_spoken
import logging


class ClearyBot(Client):
    async def on_ready(self):
        logging.warning(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # logging.warning(f'Message from {message.author}: {message.content}')
        await prophet_has_spoken(message)
