import discord
from cowsay import get_output_string, char_names
from discord import app_commands

from utils.client import tree
from utils.utils import get_server, logger, codeify


@tree.command(name="cowsay", guild=discord.Object(get_server()))
@app_commands.describe(content="The content to cowsay")
@app_commands.describe(
    character=f"The character to print instead of a cow. Valid characters are: {char_names}"
)
async def cowsay(
    interaction: discord.Interaction, content: str, character: str = "cow"
) -> None:
    # lower() is not the preferred method of case insensitive case
    # comparison, but unfortunately cowsay appears to use lower() in
    # get_output_string() instead of casefold().
    if character.lower() not in char_names:
        await interaction.response.send_message(
            f"Invalid character name, I don't know {character}! Valid character names are: {char_names}"
        )
        logger.info(f"Invalid character requested for cowsay: {character}")
        return
    await interaction.response.send_message(
        codeify(get_output_string(character, content))
    )
    logger.info("Cowsay activated!")


@cowsay.error
async def cowsay_error(ctx, error):
    logger.error(error)
    await ctx.send(
        f"An unknown error has occured! Ping nick and tell him he's a dipshit! Because you're all intelligent: here's the error: {error}"
    )
