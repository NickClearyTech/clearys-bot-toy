import discord
from github import Github, Auth

from config.get_config import config_object
from utils.client import tree
from utils.utils import get_server, logger


@tree.command(name="redploy", guild=discord.Object(get_server()))
async def redeploy(interaction: discord.Interaction):
    logger.info("Starting redeploy")
    await interaction.response.send_message("I'm redeploying myself. Go fuck yourself.")
    auth = Auth.Token(config_object.github.token)
    g = Github(auth=auth)

    repo = g.get_organization(config_object.github.owner).get_repo(
        config_object.github.repo
    )

    for workflow in repo.get_workflows():
        if workflow.name == config_object.github.workflow_name:
            workflow.create_dispatch(ref="main")

    await interaction.channel.send("Successfully started redeploy")
