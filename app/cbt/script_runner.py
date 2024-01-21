"""
This file is intended to be built and run locally for script purposes
For example, loading all the messages from the discord server into the DB
"""
from metrics.users import upload_all_users
from metrics.messages import get_all_messages
from utils.client import client
from utils.utils import get_token, log_handler, logger, init_logger, get_chance

# Importing this here ends up creating the config object
from config import get_config


@client.event
async def on_ready():
    await upload_all_users(client)
    await get_all_messages(client)

init_logger()
try:
    client.run(get_token(), log_handler=log_handler)
except Exception as e:
    logger.critical(e)
