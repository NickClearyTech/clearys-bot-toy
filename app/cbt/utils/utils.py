import os
import sys
import logging
from config.get_config import config_object

logger :logging.Logger = logging.getLogger('main')
log_handler :logging.StreamHandler = logging.StreamHandler(sys.stdout)

def get_token():
    if token := os.environ.get("DISCORD_TOKEN", None) is None:
        logger.critical("ERROR: INVALID TOKEN")
        exit(1)
    return token


def get_server():
    if config_object.discord_server_id is None:
        logger.critical("ERROR: INVALID DISCORD TOKEN")
        exit(1)
    return config_object.discord_server_id


def init_logger():
    env_log_level = os.environ.get("LOG_LEVEL", None).upper

    if env_log_level == "CRITICAL":
        logger.setLevel(logging.CRITICAL)
    elif env_log_level == "ERROR":
        logger.setLevel(logging.ERROR)
    elif env_log_level == "WARNING" or env_log_level == "WARN":
        logger.setLevel(logging.WARNING)
    elif env_log_level == "INFO":
        logger.setLevel(logging.INFO)
    elif env_log_level == "DEBUG":
        logger.setLevel(logging.DEBUG)
    else:
        logging.info("No log level provided. Defaulting to INFO.")
        logger.setLevel(logging.INFO)
        

# Wraps a set of text in a code block
# This avoid issues with double slashes \\, that the discord util escape markdown does not handle
def codeify(text: str):
    return f"```{text}```"
