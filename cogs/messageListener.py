import discord
from discord.ext import commands
import json

class MessageListener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.channel.id == json.loads(open('config.json').read())['verifyChannelID']:
            if message.content.lower() == '&verify':
                await message.author.add_roles(message.guild.get_role(json.loads(open('config.json').read())['verifyRoleID']), reason='verified')
                await message.author.guild.get_channel(json.loads(open('config.json').read())['welcomeMsgChannelID']).send(f'{message.author.mention}, **whalecum to `Code Cave` 🐳💦**')
                await message.delete()
            else:
                if message.author.id != 776418566349127690:
                    await message.delete()
        elif 'good dog' in message.content.lower():
                with open('media/sip.png', 'rb') as f:
                    await message.channel.send(file=discord.File(f))
        elif 'bad dog' in message.content.lower():
                with open('media/crying.png', 'rb') as f:
                    await message.channel.send(file=discord.File(f))
        elif 'cerberus' in message.content.lower():
            await message.channel.send(json.loads(open('config.json').read())['eventNameEmote'])

def setup(client):
    client.add_cog(MessageListener(client))