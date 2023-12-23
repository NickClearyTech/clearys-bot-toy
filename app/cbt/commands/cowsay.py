import logging

from cowsay import get_output_string, char_names

from discord.ext import commands
from discord.ext.commands.context import Context

from utils.utils import codeify


@commands.command(pass_context=True)
async def cowsay(ctx: Context, *args):
    # Assume a cowsay
    if len(args) == 1:
        await ctx.send(codeify(get_output_string("cow", args[0])))
        return
    # Specifying a characters a second a parameter
    elif len(args) == 2:
        # Check for valid character
        char_name: str = args[1].lower()
        if char_name not in char_names:
            await ctx.send(
                f"I do not know character {char_name}. The available characters are: {char_names}"
            )
            logging.warning(f"Invalid character requested for cowsay: {char_name}")
            return
        await ctx.send(codeify(get_output_string(char_name, args[0])))
    else:
        await ctx.send(f"Too many parameters provided!")


@cowsay.error
async def cowsay_error(ctx, error):
    logging.error(error)
    await ctx.send(
        f"An unknown error has occured! Ping nick and tell him he's a dipshit! Because you're all intelligent: here's the error: {error}"
    )
