from discord.ext import commands

class OwnerAccess(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def invokeEvent(self, ctx, eventName, *, args):
        self.client.dispatch(eventName, args)

        await ctx.channel.send(':thumbsup: event called.')

def setup(client):
    client.add_cog(OwnerAccess(client))