import discord
from cowsay import get_output_string, char_names
from discord import app_commands
from utils.client import tree
from utils.utils import get_server, logger
from utils.text_manipulations import codeify, translate_text


@tree.command(name="cowsay", guild=discord.Object(get_server()))
@app_commands.describe(content="The content to cowsay")
@app_commands.describe(
    character=f"The character to print instead of a cow. Valid characters are: {char_names}"
)
@app_commands.describe(
    output_language="the language for the command to translate to. Defaults to not translating the text."
)
async def cowsay(
    interaction: discord.Interaction,
    content: str,
    character: str = "cow",
    output_language: str = None,
) -> None:
    # lower() is not the preferred method of case insensitive case
    # comparison, but unfortunately cowsay appears to use lower() in
    # get_output_string() instead of casefold().
    if character.lower() not in char_names:
        await interaction.response.send_message(
            await translate_text(
                "Invalid character name, I don't know", output_language
            )
            + " "
            + character
            + "! "
            + await translate_text("Valid character names are ", output_language)
            + ": "
            + str(char_names)
        )
        logger.info(f"Invalid character requested for cowsay: {character}")
        return
    await interaction.response.send_message(
        codeify(
            get_output_string(character, await translate_text(content, output_language))
        )
    )
    logger.info("Cowsay activated!")


@cowsay.error
async def cowsay_error(ctx, error: str):
    logger.error(error)
    await ctx.send(
        f"An unknown error has occured! Ping nick and tell him he's a dipshit! Because you're all intelligent: here's the error: {error}"
    )
