import asyncio
import sys
import random

import discord

from utils import bot_activities
from utils.client import tree, client
from utils.utils import get_token, get_server
from discord import Status, CustomActivity
from message_handlers import __handlers__
from config.get_config import get_config

import logging

handler = logging.StreamHandler(sys.stdout)
handler.level = logging.INFO


@client.event
async def on_ready():
    logging.warning(f"Loaded {len(__handlers__)} handlers")
    await client.change_presence(
        status=Status.online,
        activity=CustomActivity(name=random.choice(bot_activities.bot_activites)),
    )
    import commands

    await tree.sync(guild=discord.Object(get_server()))
    logging.warning("Ready!")


@client.event
async def on_message(message: discord.Message):
    logging.warning(f"Message from {message.author}: {message.content}")
    # If bot, we don't care, return
    if message.author.bot:
        return
    # Retrieve the individual handlers,imports them, and the decorator handles whether the actual functions run
    for _, module, func_name in __handlers__:
        handler = getattr(sys.modules[module], func_name)
        await handler(message)

get_config()
client.run(get_token(), log_handler=handler)
