import sys

import discord
from bot import ClearyBot
from message_handlers import load, __handlers__
from utils.utils import get_token

import logging

handler = logging.StreamHandler(sys.stdout)

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    client = ClearyBot(intents=intents)
    client.run(get_token(), log_handler=handler, log_level=logging.INFO)
