import discord,aiohttp
from discord.ext import commands

class HugCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def hug(self, ctx, member:discord.Member=None):
		if member == None or member == ctx.message.author:
				async with ctx.channel.typing():
					async with aiohttp.ClientSession() as cs:
						async with cs.get("https://neko-love.xyz/api/v1/hug") as r:
							data = await r.json()

							embed = discord.Embed(title=f"{ctx.author} is hugging themselves! UwU", colour=0x6FB900)
							embed.set_image(url=data['url'])

							await ctx.send(embed=embed)
		else:
			async with ctx.channel.typing():
				async with aiohttp.ClientSession() as cs:
					async with cs.get("https://neko-love.xyz/api/v1/hug") as r:
						data = await r.json()

			embed = discord.Embed(title=f"{ctx.author} is hugging {member}! UwU", colour=0x6FB900)
			embed.set_image(url=data['url'])

			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(HugCom(bot))
	print('Hug Commands Loaded Successfully!')
