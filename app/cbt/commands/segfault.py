import discord

from discord import app_commands

from utils.client import tree
from utils.utils import get_server, logger

@tree.command(name="segfault", guild=discord.Object(get_server()))
async def segfault(
    interaction: discord.Interaction
):
    await interaction.response.send_message("BRB KMS")
    logger.info("Segfault triggered")
    import ctypes;ctypes.string_at(0)
    logger.info("We failed to segfault. Cry about it!")

