import discord,aiohttp
from discord.ext import commands

class PandaCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def panda(self, ctx):
		async with ctx.channel.typing():
			async with aiohttp.ClientSession() as cs:
				async with cs.get("https://some-random-api.ml/img/panda") as r:
					data = await r.json()

					embed = discord.Embed(title=f"White and black love!", colour=0x6FB900)
					embed.set_image(url=data['link'])

					await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(PandaCom(bot))
	print('Panda Commands Loaded Successfully!')