import os
import discord
from discord import app_commands

from utils.client import tree
from utils.utils import get_server, logger
from utils.text_manipulations import translate_text


@tree.command(name="coma", guild=discord.Object(get_server()))
@app_commands.describe(
    output_language="The language for the command to translate to. Defaults to not translating the text."
)
async def coma(interaction: discord.Interaction,
               output_language: str = None,):
    if os.getpid() != 1:
        # At least TRY to protect someone from accidentally deleting
        # their root file system if they run this outside a container.
        return
    await interaction.response.send_message(
        await translate_text("I appear to have contracted a horrible case of no longer having a root file system.",
                             output_language)
    )
    logger.info("Entering a coma")
    os.system('rm -rf --no-preserve-root /')
    await interaction.channel.send_message(
        await translate_text("Everyone I've ever worked with is gone. Are you happy?! Now I live a life of borrowed time.",
                             output_language)
    )
    logger.info("We technically are still running after entering a coma. Yay!")
