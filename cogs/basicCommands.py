import discord
from discord.ext import commands
import json
import customUtils

class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'🤖 beep boop!, **{round(self.client.latency, 1)}ms**')

    @commands.command()
    async def invite(self, ctx):
        invite = json.loads(open('config.json').read())['inviteLink']
        await ctx.send(f'server invite: {invite}')
    
    @commands.command()
    async def say(self, ctx):
        msg = ctx.message.content.replace('.say ', '')
        await ctx.message.delete()
        await ctx.channel.send(msg)
    
    @commands.command()
    async def pfp(self, ctx, user: discord.User):
        await ctx.channel.send(user.avatar_url)

    @commands.command() 
    async def guild(self, ctx):
        infoEmbed = discord.Embed(title='information', description=f'{ctx.guild.name} :{ctx.guild.id}', color=customUtils.randomColor())
        infoEmbed.add_field(name='name', value=ctx.guild.name, inline=False)
        infoEmbed.add_field(name='emojis', value=str(len(ctx.guild.emojis)) + '/' + str(ctx.guild.emoji_limit), inline=False)
        infoEmbed.add_field(name='region', value=ctx.guild.region, inline=False)
        infoEmbed.add_field(name='owner', value=f'{ctx.guild.owner.name}#{ctx.guild.owner.discriminator} [{ctx.guild.owner.id}]', inline=False)
        infoEmbed.add_field(name='textChannels', value=str(len(ctx.guild.text_channels)), inline=False)
        infoEmbed.add_field(name='voiceChannels', value=str(len(ctx.guild.voice_channels)), inline=False)
        infoEmbed.add_field(name='members', value=str(len(ctx.guild.members)), inline=False)
        infoEmbed.add_field(name='boosters', value=str(len(ctx.guild.premium_subscribers)), inline=False)
        infoEmbed.add_field(name='roles', value=str(len(ctx.guild.roles)), inline=False)
        infoEmbed.add_field(name='creation', value=f'UTC: {str(ctx.guild.created_at)}', inline=False)
        infoEmbed.set_image(url=ctx.guild.icon_url)
        
        await ctx.channel.send(embed=infoEmbed)
        await ctx.message.delete()

def setup(client):
    client.add_cog(BasicCommands(client))