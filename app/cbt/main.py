import sys
import random

import discord

from utils import bot_activities
from utils.client import tree, client
from utils.utils import (
    get_token,
    get_server,
    log_handler,
    logger,
    init_logger,
    get_chance,
)
from utils.text_manipulations import get_languages, translate_text
from discord import Status, CustomActivity
from message_handlers import __handlers__

# Importing this here ends up creating the config object
from config import get_config


@client.event
async def on_ready():

    logger.info(f"Loaded {len(__handlers__)} handlers")

    await client.change_presence(
        status=Status.online,
        activity=CustomActivity(
            name=await translate_text(
                random.choice(bot_activities.bot_activites),
                (
                    "en"
                    if not get_chance(percent=10)
                    else random.choice(list((await get_languages()).keys()))
                ),
            )
        ),
    )
    import commands

    await tree.sync(guild=discord.Object(get_server()))
    logger.info("Ready!")


@client.event
async def on_message(message: discord.Message):
    logger.debug(f"Message from {message.author}: {message.content}")
    # If bot, we don't care, return
    if message.author.bot:
        return
    # Retrieve the individual handlers,imports them, and the decorator handles whether the actual functions run
    for _, module, func_name in __handlers__:
        handler = getattr(sys.modules[module], func_name)
        await handler(message)


init_logger()
try:
    client.run(get_token(), log_handler=log_handler)
except Exception as e:
    logger.critical(e)
