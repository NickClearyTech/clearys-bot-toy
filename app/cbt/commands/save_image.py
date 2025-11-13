import discord
from discord import app_commands
from utils.client import tree
from utils.utils import get_server, logger


@tree.command(name="save_image", guild=discord.Object(get_server()))
@app_commands.describe(image_name="Image name")
@app_commands.describe(image_file="Image file to upload")
async def save_image(
    interaction: discord.Interaction, image_name: str, image_file: discord.Attachment
) -> None:
    logger.info(f"Saving image: {image_name}")

    await interaction.response.send_message("Saving image")


@save_image.error
async def cowsay_error(ctx, error: str):
    logger.error(error)
    await ctx.send(
        f"An unknown error has occured! Ping nick and tell him he's a dipshit! Because you're all intelligent: here's the error: {error}"
    )
