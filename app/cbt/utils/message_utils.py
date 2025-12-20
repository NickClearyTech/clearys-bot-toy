from urllib.parse import urlparse
from discord import Message
from utils.utils import logger


def message_has_urls(message: Message) -> bool:
    logger.debug(f"Checking if message {message.content} has urls")
    splitted = message.content.split(" ")
    for word in splitted:
        parsed = urlparse(word)
        if parsed.scheme and parsed.netloc:
            logger.debug(f"Found URL: {word}")
            return True
    return False


def get_all_urls_in_message(message: Message):
    urls = []
    splitted = message.content.split(" ")
    for word in splitted:
        parsed = urlparse(word)
        if parsed.scheme and parsed.netloc:
            urls.append(word)
    return urls
