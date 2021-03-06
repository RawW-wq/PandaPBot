import discord
import aiohttp
from discord.ext import commands

class SlapCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def slap(self, ctx, member:discord.Member=None):
		if member == None or member == ctx.message.author:
			await ctx.send('Why did you slap yourself... ? :/')
		else:
			async with ctx.channel.typing():
				async with aiohttp.ClientSession() as cs:
					async with cs.get("https://neko-love.xyz/api/v1/slap") as r:
						data = await r.json()

			embed = discord.Embed(title=f"{ctx.author} is slapping {member}! Nuuu :(", colour=0x6FB900)
			embed.set_image(url=data['url'])

			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(SlapCom(bot))
	print('Slap Command Loaded Successfully!')
