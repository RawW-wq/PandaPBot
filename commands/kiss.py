import discord
import aiohttp
from discord.ext import commands

class KissCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def kiss(self, ctx, member:discord.Member=None):
		if member == None or member == ctx.message.author:
			await ctx.send('Tell me.. How the fuck you can kiss yourself?!?')
		else:
			async with ctx.channel.typing():
				async with aiohttp.ClientSession() as cs:
					async with cs.get("https://neko-love.xyz/api/v1/kiss") as r:
						data = await r.json()

			embed = discord.Embed(title=f"{ctx.author} is kissing {member}! Love is in the air <3", colour=0x6FB900)
			embed.set_image(url=data['url'])

			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(KissCom(bot))
	print('Kiss Command Loaded Successfully!')
