import aiohttp

from config.get_config import config_object

import discord

from utils.utils import get_server, logger


async def check_and_upload_user(member: discord.Member, session: aiohttp.ClientSession):
    result = await session.get(
        f"{config_object.metrics_server_config.url}/user/{member.id}"
    )

    user_data = {
        "date_joined": member.joined_at.strftime("%Y-%m-%d %H:%M:%S"),
        "is_bot": member.bot,
    }
    # If the user doesn't exist, create it
    if not result.ok:
        user_data["user_id"] = str(member.id)
        create_result = await session.post(
            f"{config_object.metrics_server_config.url}/user", json=user_data
        )
        if create_result.ok:
            logger.info(f"User {member.id} created successfully")
        else:
            logger.error(
                f"Error creating user object: {user_data}. Error {await create_result.json()}"
            )
            exit(1)
    else:
        update_result = await session.patch(
            f"{config_object.metrics_server_config.url}/user/{member.id}",
            json=user_data,
        )
        if update_result.ok:
            logger.info(f"User {member.id} updated successfully")
        else:
            logger.error(
                f"Error updating user object: {user_data}. Error {await update_result.json()}"
            )
            exit(1)


async def upload_all_users(client: discord.Client):
    async with aiohttp.ClientSession() as session:
        # Assume just one server for now, easier
        guild = await client.fetch_guild(get_server())
        async for member in guild.fetch_members(limit=150):
            await check_and_upload_user(member, session)
