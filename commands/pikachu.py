import discord,aiohttp
from discord.ext import commands

class PikachuCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def pikachu(self, ctx):
		async with ctx.channel.typing():
			async with aiohttp.ClientSession() as cs:
				async with cs.get("https://some-random-api.ml/img/pikachu") as r:
					data = await r.json()

					embed = discord.Embed(title=f"PI-KA-CHUUU", colour=0x6FB900)
					embed.set_image(url=data['link'])

					await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(PikachuCom(bot))
	print('Pikachu Commands Loaded Successfully!')