import discord
from discord.ext import commands

class ReverseCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def reverse(self, ctx, *, text: str=None):
		t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
		if text is None:
			await ctx.send('Type me wut text do u want to reverse?')
		else:
			await ctx.send(f"{t_rev}")

def setup(bot):
	bot.add_cog(ReverseCom(bot))
	print('Reverse Command Loaded Successfully!')
