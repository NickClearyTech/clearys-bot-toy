import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
client: discord.Client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
