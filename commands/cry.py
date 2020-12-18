import discord,aiohttp
from discord.ext import commands

class CryCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def cry(self, ctx, member:discord.Member=None):
		if member == None or member == ctx.message.author:
				async with ctx.channel.typing():
					async with aiohttp.ClientSession() as cs:
						async with cs.get("https://neko-love.xyz/api/v1/cry") as r:
							data = await r.json()

							embed = discord.Embed(title=f"{ctx.author} is crying! ;c", colour=0x6FB900)
							embed.set_image(url=data['url'])

							await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(CryCom(bot))
	print('Cry Command Loaded Successfully!')
