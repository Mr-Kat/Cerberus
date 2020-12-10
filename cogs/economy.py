import discord
from discord.ext import commands
import json

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    async def createDatabase(self, ctx):
        with open('economy.json', 'w+') as f:
            entry = {}
            for _ in ctx.guild.members:
                entry[_.id] = 0
            
            json.dump(entry, f, indent=4)
        await ctx.channel.send('👍 successfully created database')

    @commands.command()
    @commands.is_owner()
    async def showBalance(self, ctx, uid: int):
        with open('economy.json', 'r') as f:
            try:
                await ctx.channel.send(f'balance for {str(uid)}: ' + str(json.load(f)[str(uid)]))
            except IndexError:
                await ctx.channel.send('user not found')

    @commands.command()
    @commands.is_owner()
    async def addBalance(self, ctx, uid: int, amount: int):
        with open('economy.json', 'w') as f:
            entry = json.load(f)
            entry[str(uid)] += amount

            json.dump(entry, f, indent=4)
    
    @commands.command()
    @commands.is_owner()
    async def subBalance(self, ctx, uid: int, amount: int):
        with open('economy.json', 'w') as f:
            entry = json.load(f)
            entry[str(uid)] -= amount

            json.dump(entry, f, indent=4)

def setup(client):
    client.add_cog(Economy(client))