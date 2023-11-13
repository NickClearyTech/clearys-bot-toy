import sys

import discord
from bot import ClearyBot
from utils.utils import get_token
from commands.cowsay import cowsay

import logging

handler = logging.StreamHandler(sys.stdout)

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    bot = ClearyBot(command_prefix="/", intents=intents)

    # Register commands
    # theres probably a way to do this dynamically but idgaf
    bot.add_command(cowsay)

    bot.run(get_token(), log_handler=handler, log_level=logging.INFO)
