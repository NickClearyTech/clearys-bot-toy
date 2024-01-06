import discord
from github import Github, Auth
from discord import app_commands

from config.get_config import config_object
from utils.client import tree
from utils.utils import get_server, logger
from utils.text_manipulations import translate_text


@tree.command(name="redploy", guild=discord.Object(get_server()))
@app_commands.describe(
    output_language="the language for the command to translate to. Defaults to not translating the text."
)
async def redeploy(interaction: discord.Interaction, output_language: str = None):
    logger.info("Starting redeploy")
    await interaction.response.send_message(
        await translate_text(
            "I'm redeploying myself. Go fuck yourself.", output_language
        )
    )
    auth = Auth.Token(config_object.github.token)
    g = Github(auth=auth)

    repo = g.get_organization(config_object.github.owner).get_repo(
        config_object.github.repo
    )

    for workflow in repo.get_workflows():
        if workflow.name == config_object.github.workflow_name:
            workflow.create_dispatch(ref="main")

    await interaction.channel.send(
        await translate_text("Successfully started redeploy", output_language)
    )
