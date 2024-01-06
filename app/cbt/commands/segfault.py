import discord
from discord import app_commands

from utils.client import tree
from utils.utils import get_server, logger, get_chance
from utils.text_manipulations import translate_text


@tree.command(name="segfault", guild=discord.Object(get_server()))
@app_commands.describe(
    output_language="the language for the command to translate to. Defaults to not translating the text."
)
async def segfault(interaction: discord.Interaction, output_language: str = None):
    if get_chance():
        await interaction.response.send_message(translate_text("No u", output_language))
        return
    await interaction.response.send_message(translate_text("BRB KMS", output_language))
    logger.info("Segfault triggered")
    import ctypes

    ctypes.string_at(0)
    logger.info("We failed to segfault. Cry about it!")
