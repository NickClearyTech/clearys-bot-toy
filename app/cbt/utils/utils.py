import os
import sys
import logging
from config.get_config import config_object

logger :logging.Logger = logging.getLogger('main')
log_handler :logging.StreamHandler = logging.StreamHandler(sys.stdout)

def get_token():
    if (token := os.environ.get("DISCORD_TOKEN", None)) is None:
        logger.critical("ERROR: INVALID TOKEN")
        exit(1)
    logger.debug(f"Token is {token}")
    return token


def get_server():
    if config_object.discord_server_id is None:
        logger.critical("ERROR: INVALID DISCORD TOKEN")
        exit(1)
    logger.debug(f"Server is {config_object.discord_server_id}")
    return config_object.discord_server_id


def init_logger():
    logger.addHandler(log_handler)
    env_log_level = os.environ.get("LOG_LEVEL", "INFO")

    match env_log_level:
        case "CRITICAL":
            logger.setLevel(logging.CRITICAL)
        case "ERROR":
            logger.setLevel(logging.ERROR)
        case "WARNING" | "WARN":
            logger.setLevel(logging.WARNING)
        case "INFO":
            logger.setLevel(logging.INFO)
        case "DEBUG":
            logger.setLevel(logging.DEBUG)
        case _:
            logger.setLevel(logging.INFO)
            

# Wraps a set of text in a code block
# This avoid issues with double slashes \\, that the discord util escape markdown does not handle
def codeify(text: str):
    return f"```{text}```"
