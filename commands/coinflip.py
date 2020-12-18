import discord,random
from discord.ext import commands

class CoinCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True, aliases=['flip', 'cf'])
	async def coinflip(self, ctx):
		choices = ('HEADS', 'TAILS')
		rancoin = random.choice(choices)
		embed = discord.Embed(description=f'The coin landed on... **{rancoin}**', color=0x6FB900)
		await ctx.send(embed=embed)
        
	@commands.command()
	async def cftest(self, ctx):
		embed = discord.Embed(description = 'Zdr testa bachka', colour = 0x6FB900)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(CoinCom(bot))
	print('CoinFlip Commands Loaded Successfully!')
