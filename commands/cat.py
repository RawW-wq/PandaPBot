import discord,aiohttp
from discord.ext import commands

class CatCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def cat(self, ctx):
		async with ctx.channel.typing():
			async with aiohttp.ClientSession() as cs:
				async with cs.get("https://some-random-api.ml/img/cat") as r:
					data = await r.json()

					embed = discord.Embed(title=f"Some adorable cats!", colour=0x6FB900)
					embed.set_image(url=data['link'])

					await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(CatCom(bot))
	print('Cat Commands Loaded Successfully!')