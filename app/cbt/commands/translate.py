import discord
from discord import app_commands

from utils.client import tree
from utils.utils import get_server, logger
from utils.text_manipulations import translate_text, get_languages


@tree.command(name="translate", guild=discord.Object(get_server()))
@app_commands.describe(content="The content to translate")
@app_commands.describe(
    input_language_code="the language of the text to translate. Default is auto-detect"
)
@app_commands.describe(output_language_code="the language for the command to output")
async def translate(
    interaction: discord.Interaction,
    content: str,
    output_language_code: str,
    input_language_code: str = "auto",
) -> None:
    await interaction.response.send_message(
        await translate_text(
            content, output_language_code, source_language_in=input_language_code
        )
    )
    logger.info(f"{input_language_code} -> {output_language_code}: {content[30:]}")


@translate.error
async def translate_error(ctx, error: str):
    logger.error(error)
    await ctx.send(
        f"An unknown error has occured! Ping nick and tell him he's a dipshit! Because you're all intelligent: here's the error: {error}"
    )


@tree.command(name="get_languages", guild=discord.Object(get_server()))
@app_commands.describe(
    language_code="the source language code to find destinations for. If empty, displays valid list of source languages"
)
async def get_languages_command(
    interaction: discord.Interaction,
    language_code: str = None,
) -> None:
    languages = await get_languages()
    source_language_list = [
        f"{code} ({languages[code]['name']})" for code in languages.keys()
    ]

    if language_code is not None:
        language_code = language_code.casefold()
        logger.info(f"Getting target languages for {language_code}")
        if language_code not in languages.keys():
            await interaction.response.send_message(
                f"Invalid source language. Valid source languages are {source_language_list}"
            )
        else:
            target_language_list = [
                f"{code} ({languages[code]['name']})"
                for code in languages[language_code]["targets"]
            ]
            await interaction.response.send_message(
                f"Valid target languages for {language_code} ({languages[language_code]['name']}) are {target_language_list}"
            )
    else:
        logger.info(f"Getting source languages")
        await interaction.response.send_message(
            f"Valid source languages are {source_language_list}"
        )


@get_languages_command.error
async def get_languages_command_error(ctx, error: str):
    logger.error(error)
    await ctx.send(
        f"An unknown error has occured! Ping nick and tell him he's a dipshit! Because you're all intelligent: here's the error: {error}"
    )
