import aiohttp
import discord
from config.get_config import config_object
from utils.utils import get_server, logger


async def upload_message_to_metrics(message: discord.Message) -> None:
    async with aiohttp.ClientSession() as session:
        message_data = {
            "message_id": str(message.id),
            "user_id": str(message.author.id),
            "contents": message.content,
            "channel_id": str(message.channel.id),
            "sent_at": message.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        if message.reference is not None:
            message_data["in_reply_to"] = str(message.reference.message_id)

        result = await session.post(
            f"{config_object.metrics_server_config.url}/message", json=message_data
        )

        if not result.ok:
            logger.error(
                f"Error uploading message: {message_data} with error: {await result.json()}"
            )
            return
        logger.info(f"Successfully uploaded message {message.id} to metrics server")


async def get_all_messages(client: discord.Client):
    channels = (await client.fetch_guild(get_server())).channels.all()
    for channel in channels:
        logger.info(f"{channel.name}")