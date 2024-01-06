import discord

from discord import app_commands

from utils.client import tree
from utils.utils import get_server, logger
from utils.text_manipulations import translate_text
from datetime import timedelta


@tree.command(name="pyramid_user", guild=discord.Object(get_server()))
@app_commands.describe(user="The user to pyramid")
@app_commands.describe(depth="The depth of the pyramid")
@app_commands.describe(
    output_language="the language for the command to translate to. Defaults to not translating the text."
)
async def pyramid_user(
    interaction: discord.Interaction,
    user: discord.Member,
    depth: int = 8,
    output_language: str = None,
):
    logger.info("Pyramid requested for user")
    if depth > 12:
        await interaction.response.send_message(
            await translate_text(
                "Maximum supported depth is 13! Otherwise wierd formatting bullshit looks ugly. Also it fucks with my rate limit",
                output_language,
            )
        )
        return
    if depth < 2:
        await interaction.response.send_message(
            await translate_text(
                "Depth must be at least 2, otherwise it's not really a pyramid. Then it's just a sad sack of shit.",
                output_language,
            )
        )
    await interaction.response.send_message(
        await translate_text(
            "On it! Gonna make the egyptians jealous!", output_language
        )
    )
    message_template = f"<@{user.id}> "
    for i in range(1, depth + 1):
        message_content = message_template * i
        await interaction.channel.send(message_content)
    for i in range(depth - 1, 0, -1):
        message_content = message_template * i
        await interaction.channel.send(message_content)
    logger.info("Pyramid completed")
