import functools
import importlib
import logging
import pkgutil
import inspect
from typing import Callable, List

from attr.converters import optional
from discord import Message

from .message_handler import message_handler

__handlers__ = []


# These must be located in this file, based on the way python handles package logic


# A decorator that wraps each potential function to respond to a message
# Checks before each function is run for whether a given message is in a list of channels, users, or servers
def handler(
    name: str,
    channels: optional(List[str]) = None,
    servers: optional(list[str]) = None,
    users: optional(list[str]) = None,
) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def run_checks(*args, **kwargs):
            if len(args) == 0:
                return None
            message: Message = args[0]
            if not isinstance(message, Message):
                return None
            if channels is not None and message.channel.id not in channels:
                return None
            if users is not None and message.author.id not in users:
                return None
            if servers is not None and message.guild.id not in servers:
                return None
            logging.warning(f"Running handler: {name}")
            return await func(*args, **kwargs)

        __handlers__.append((name, inspect.getmodule(func).__name__, func.__name__))
        return run_checks

    return wrapper


# Loads all handlers
def load() -> None:
    __all__ = []
    for _, module_name, _ in pkgutil.walk_packages(__path__):
        __all__.append(module_name)
        _module = importlib.import_module(f"{__name__}.{module_name}")
        globals()[module_name] = _module
