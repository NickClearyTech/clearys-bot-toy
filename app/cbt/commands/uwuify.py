import discord
import uwuify
from discord import app_commands

from utils.client import tree
from utils.utils import get_server, logger


@tree.command(name="uwuify_text", guild=discord.Object(get_server()))
@app_commands.describe(text="The text to uwuify")
@app_commands.describe(smiley="Whether to add a smiley at the end")
@app_commands.describe(yu="Whether to convert u's to yu's")
@app_commands.describe(stutter="Whether to make the text stutter")
async def uwuify_text(
    interaction: discord.Interaction,
    text: str,
    smiley: bool = False,
    yu: bool = False,
    stutter: bool = False,
):
    logger.info("UwUify called")

    if not text.endswith(".") and not text.endswith("!") and not text.endswith("?"):
        text += "."

    flags = uwuify.UwuifyFlag.NONE
    if smiley:
        flags = flags | uwuify.SMILEY
    if yu:
        flags = flags | uwuify.YU
    if stutter:
        flags = flags | uwuify.STUTTER
    result = uwuify.uwu(text, flags=flags)

    await interaction.response.send_message(result)


@uwuify_text.error
async def uwuify_text_error(ctx, error):
    logger.error(error)
    await ctx.send(
        f"An unknown error has occured! Man, you suck. But nick sucks more. Tell him he's a dumbass! Your error is: {error}. How did you manage that, you fuck?"
    )
