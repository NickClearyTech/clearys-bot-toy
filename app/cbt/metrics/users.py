import logging

import aiohttp

from config.get_config import config_object

import discord

from utils.utils import get_server


async def check_and_upload_user(member: discord.Member, session: aiohttp.ClientSession):
    result = await session.get(
        f"{config_object.metrics_server_config.url}/user/{member.id}"
    )
    # If the user doesn't exist, create it
    if result.status != 200:
        user_data = {
            "user_id": str(member.id),
            "date_joined": member.joined_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        create_result = await session.post(
            f"{config_object.metrics_server_config.url}/user", json=user_data
        )
        if create_result.status == 201:
            logging.warning(f"User {member.id} created successfully")
        else:
            logging.error(
                f"Error creating user object: {user_data}. Error {await create_result.json()}"
            )
            exit(1)

    else:
        logging.warning(f"User with ID {member.id} already exists")


async def upload_all_users(client: discord.Client):
    async with aiohttp.ClientSession() as session:
        # Assume just one server for now, easier
        members = (await client.fetch_guild(get_server())).members
        guild = await client.fetch_guild(get_server())
        async for member in guild.fetch_members(limit=150):
            await check_and_upload_user(member, session)
