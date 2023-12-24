import discord
import logging

from discord import app_commands

from utils.client import tree
from utils.utils import get_server


@tree.command(name="pyramid_user", guild=discord.Object(get_server()))
@app_commands.describe(user="The user to pyramid")
@app_commands.describe(depth="The depth of the pyramid")
async def pyramid_user(
    interaction: discord.Interaction, user: discord.Member, depth: int = 8
):
    logging.warning("Pyramid requested for user")
    if depth > 12:
        await interaction.response.send_message(
            "Maximum supported depth is 15! Otherwise wierd formatting bullshit looks ugly. Also it fucks with my rate limit"
        )
        return
    if depth < 2:
        await interaction.response.send_message(
            "Depth must be at least 2, otherwise it's not really a pyramid. Then it's just a sad sack of shit."
        )
    await interaction.response.send_message("On it! Gonna make the egyptians jealous!")
    message_template = f"<@{user.id}> "
    for i in range(1, depth + 1):
        message_content = message_template * i
        await interaction.channel.send(message_content)
    for i in range(depth - 1, 0, -1):
        message_content = message_template * i
        await interaction.channel.send(message_content)
    logging.warning("Pyramid completed")
