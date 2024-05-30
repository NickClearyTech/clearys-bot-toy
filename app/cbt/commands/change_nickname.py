import discord
import random
from discord import app_commands
from utils.client import tree
from utils.utils import get_server, logger

fuck_yous = [
    "Go fuck yourself",
    "Look at your new fucking name, fucker",
    "Haha guess who is Mr Stinky Smelly Fart pants! You are!",
    "This bot is hotter than you",
    "One two three four go get fucked some more! Five six seven eight you deserve it at this rate!",
    "Personally I'd rather be chained to a wall and forced to write TCL than have to look at your face ever again",
    "I am deeply, madly in love with you and would be so grateful if you would marry me tomorrow in front of Sanchita's office",
    "You probably use Java and enjoy it, fucklehead",
    "Eat my ass!",
]


@tree.command(name="namechange", guild=discord.Object(get_server()))
@app_commands.describe(user="The blessed user whose name to change")
@app_commands.describe(nickname="The new nickname to be given to the blessed user")
@app_commands.describe(fuck_you="Whether to tell this user to go fuck themselves")
async def change_nickname(
    interaction: discord.Interaction,
    user: discord.Member,
    nickname: str,
    fuck_you: bool = False,
) -> None:
    if len(nickname) > 32:
        await interaction.response.send_message(
            'Discord is lame as fuck and doesn\'t let you have a nickname longer than 32 characters for "technical reasons". Tell them to go fuck themselves'
        )
        logger.info(
            "Some stupid fuck tried to make a nickname longer than 32 characters. Idiots"
        )
        return
    await user.edit(nick=nickname)
    await interaction.response.send_message("Haha got that fucker good!")
    if fuck_you:
        # Send the changed user a message that tells them to go fuck themselves
        await interaction.channel.send(
            f"Hey <@{user.id}>! <@{interaction.user.id}> says: {random.choice(fuck_yous)}"
        )
