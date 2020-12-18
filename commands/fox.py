import discord,aiohttp
from discord.ext import commands

class FoxCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def fox(self, ctx):
		async with ctx.channel.typing():
			async with aiohttp.ClientSession() as cs:
				async with cs.get("https://some-random-api.ml/img/fox") as r:
					data = await r.json()

					embed = discord.Embed(title=f"What does the fox say?", colour=0x6FB900)
					embed.set_image(url=data['link'])

					await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(FoxCom(bot))
	print('Fox Commands Loaded Successfully!')