import discord
import aiohttp
from discord.ext import commands

class PatCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def pat(self, ctx, member:discord.Member=None):
		if member == None or member == ctx.message.author:
				async with ctx.channel.typing():
					async with aiohttp.ClientSession() as cs:
						async with cs.get("https://neko-love.xyz/api/v1/pat") as r:
							data = await r.json()

							embed = discord.Embed(title=f"{ctx.author} pats themselves! UwU", colour=0x6FB900)
							embed.set_image(url=data['url'])

							await ctx.send(embed=embed)
		else:
			async with ctx.channel.typing():
				async with aiohttp.ClientSession() as cs:
					async with cs.get("https://neko-love.xyz/api/v1/pat") as r:
						data = await r.json()

			embed = discord.Embed(title=f"{ctx.author} pats {member}! Cute :3", colour=0x6FB900)
			embed.set_image(url=data['url'])

			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(PatCom(bot))
	print('Pat Command Loaded Successfully!')
