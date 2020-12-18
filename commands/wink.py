import discord,aiohttp
from discord.ext import commands

class WinkCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def wink(self, ctx, member:discord.Member=None):
		if member == None or member == ctx.message.author:
				async with ctx.channel.typing():
					async with aiohttp.ClientSession() as cs:
						async with cs.get("https://some-random-api.ml/animu/wink") as r:
							data = await r.json()

							embed = discord.Embed(title=f"{ctx.author} winks on themselves! Strange, but okay.", colour=0x6FB900)
							embed.set_image(url=data['link'])

							await ctx.send(embed=embed)
		else:
			async with ctx.channel.typing():
				async with aiohttp.ClientSession() as cs:
					async with cs.get("https://some-random-api.ml/animu/wink") as r:
						data = await r.json()

			embed = discord.Embed(title=f"{ctx.author} is winking on {member}! Love is in the air <3", colour=0x6FB900)
			embed.set_image(url=data['link'])

			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(WinkCom(bot))
	print('Wink Command Loaded Successfully!')
