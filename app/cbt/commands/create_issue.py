import discord
import github
from github import Github, Auth

from discord import app_commands
from utils.client import tree
from utils.utils import get_server, logger
from config.get_config import config_object
from utils.text_manipulations import translate_text


@tree.command(name="create_github_issue", guild=discord.Object(get_server()))
@app_commands.describe(title="Issue title")
@app_commands.describe(content="Issue description contents")
@app_commands.describe(
    is_bug="Whether this issue is a bug. If false, then this is a feature request"
)
async def create_github_issue(
    interaction: discord.Interaction,
    title: str,
    content: str,
    is_bug: bool,
) -> None:
    logger.debug("Github issue requested")
    await interaction.channel.send(
        content="Request for issue received! Attempting to create now!"
    )

    auth = Auth.Token(config_object.github.token)
    g = Github(auth=auth)

    repo = g.get_organization(config_object.github.owner).get_repo(
        config_object.github.repo
    )

    title_text = f"{'[Bug]' if is_bug else '[Feature]'}: {title}"

    try:
        issue = repo.create_issue(title=title_text, body=content)
    except github.GithubException as exc:
        logger.error("Failed to create issue")
        logger.error(exc)
        await interaction.response.send_message(
            "An error occured while creating issue. Tell nick he sucks"
        )
        return

    await interaction.response.send_message(
        f"Issue created! You can find it here: {issue.html_url}. Be sure to tell Nick that he sucks and to complete the issue!"
    )
