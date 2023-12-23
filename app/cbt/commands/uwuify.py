import logging
import argparse

import uwuify

from discord.ext import commands
from discord.ext.commands.context import Context

parser = argparse.ArgumentParser()
parser.add_argument("text")
parser.add_argument("--smiley", action="store_true")
parser.add_argument("-y", "--yu", action="store_true")
parser.add_argument("--stutter", action="store_true")


@commands.command(name="uwuify")
async def uwuify_text(ctx: Context, *args) -> None:
    args = parser.parse_args(args)

    text = args.text

    if not text.endswith(".") and not text.endswith("!") and not text.endswith("?"):
        text += "."

    flags = uwuify.UwuifyFlag.NONE
    if args.smiley:
        flags = flags | uwuify.SMILEY
    if args.yu:
        flags = flags | uwuify.YU
    if args.stutter:
        flags = flags | uwuify.STUTTER
    result = uwuify.uwu(text, flags=flags)
    await ctx.send(result)


@uwuify_text.error
async def uwuify_text_error(ctx, error):
    logging.error(error)
    await ctx.send(
        f"An unknown error has occured! Man, you suck. But nick sucks more. Tell him he's a dumbass! Your error is: {error}. How did you manage that, you fuck?"
    )
