import logging

import aiohttp
import asyncio

from config.get_config import config_object

import discord


async def check_and_upload_user(member: discord.Member, session: aiohttp.ClientSession):
    result = await session.get(f"{config_object.metrics_server_config.url}/user/{member.id}")
    logging.warning(result.json())


async def upload_all_users(client: discord.Client):
    async with aiohttp.ClientSession() as session:
        # Assume just one server for now, easier
        for member in client.guilds[0].members:
            await check_and_upload_user(member, session)
