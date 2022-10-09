import functools
from discord.message import Message

import logging


def message_handler(channel=None, server=None, user=None):
    def decorator_checker(func):
        @functools.wraps(func)
        async def run_checks(*args, **kwargs):
            if len(args) == 0:
                return None
            message: Message = args[0]
            if not isinstance(message, Message):
                return None
            if channel is not None and message.channel.id != channel:
                return None
            if user is not None and message.author.id != user:
                return None
            if server is not None and message.guild.id != server:
                return None
            return await func(*args, **kwargs)
        return run_checks
    return decorator_checker
