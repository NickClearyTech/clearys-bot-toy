import os
import logging
from config.get_config import config_object


def get_token():
    if os.environ.get("DISCORD_TOKEN", None) is None:
        print("ERROR: INVALID TOKEN")
        exit(1)
    return os.environ.get("DISCORD_TOKEN", None)


def get_server():
    if config_object.discord_server_id is None:
        logging.fatal("ERROR: INVALID DISCORD TOKEN")
        exit(1)
    return config_object.discord_server_id


# Wraps a set of text in a code block
# This avoid issues with double slashes \\, that the discord util escape markdown does not handle
def codeify(text: str):
    return f"```{text}```"
