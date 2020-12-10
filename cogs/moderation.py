import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import json

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def broadcastMessage(self, ctx, *, msg):
        await ctx.message.channel.send(msg)
        await ctx.message.delete()
    
    @commands.command()
    @has_permissions(administrator=True)
    async def reformatMessage(self, ctx, msgID, *,  msgContent): 
        await ctx.message.channel.fetch_message(int(msgID)).edit(content=msgContent)

    @commands.command(aliases=['shut'])
    @has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, message='None Provided'):
        muteRole = await ctx.guild.get_role(json.load(open('config.json').read())['muteRoleID'])
        for _ in member.roles:
            await _.remove_roles(_, reason=message)
        await member.add_roles(muteRole, reason=message)
        await ctx.channel.send(f'🐶 successfully muted {member.mention} - [{ctx.message.author.mention}]')
        await ctx.message.delete()

    @commands.command(aliases=['yeet'])
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, message='None Provided'):
        name = member.display_name

        await ctx.guild.kick(member, reason=message)
        with open('media/yeet.gif', 'rb') as f:
            await ctx.channel.send(f'🐶 successfully kicked {name} - [{ctx.message.author.mention}]', file=discord.File(f))
        await ctx.message.delete()

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, message='None Provided', deleteMessages=False):
        name = member.display_name
        if not deleteMessages:
            await ctx.guild.ban(member, reason=message)
        else:
            await ctx.guild.ban(member, reason=message, delete_message_days=7)
        await ctx.channel.send(f'🐶 successfully banned {name} - [{ctx.message.author.mention}]')
        await ctx.message.delete()

    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, _id: int, message='None Provided'):
        user = await self.client.fetch_user(_id)

        await ctx.guild.unban(user, reason=message)
        await ctx.channel.send(f'🐶 successfully unbanned user with id {str(_id)} - [{ctx.message.author.mention}]')
        await ctx.message.delete()
        
def setup(client):
    client.add_cog(Moderation(client))