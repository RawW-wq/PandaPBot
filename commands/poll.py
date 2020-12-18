import discord, datetime, asyncio
from discord import Embed
from discord.ext import commands
from discord.utils import get

class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def poll(self, ctx, *, question):
        pollembed = discord.Embed(
            title="New Poll!",
            colour=discord.Color.green(),
            description="Question: {}".format(question),
            timestamp=datetime.datetime.now()
            )

        pollembed.add_field(name="Asked by:", value=f"{ctx.author.mention}", inline=False)

        msg = await ctx.send(embed=pollembed)

        await msg.add_reaction("✅")
        await msg.add_reaction("❎")

    @poll.error
    async def poll_error(self, ctx, error):
        await ctx.send(error)
        print(error)
        raise error

def setup(client):
    client.add_cog(Poll(client))