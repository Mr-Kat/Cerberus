import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
cogList = [
    'messageListener',
    'basicCommands',
    'moderation',
    'ownerAccess',
    'chess',
    'economy'
    ] # static loading in necessary for hierarchy

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='heck'))
    print(f'Bot is alive in {len(client.guilds)} guild(s)')

if __name__ == '__main__':
    for _ in cogList:
        client.load_extension('cogs.' + _)

    client.run(os.environ['TOKEN'])
