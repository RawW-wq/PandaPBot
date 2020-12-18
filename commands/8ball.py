import discord,random
from discord.ext import commands

class EightballCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['8ball'])
	async def eight(self, ctx, *, question=None):
		if question is None:
			await ctx.send('Ask me something.. Bruh')
		else:
			guild = ctx.guild
			responses = ["Probably", "Probably Not", "No", "Yes", "Don't know"]
			embed = discord.Embed(title = f"8Ball {guild.name}", color = 0x000000)
			embed.set_thumbnail(url = "https://i.ibb.co/M5zfTst/1200px-8-ball-icon-svg.png")
			embed.add_field(name = f"Question = {question}", value = f"Answer = {random.choice(responses)}")

			await ctx.send(embed=embed)

	@eight.error
	async def eight_error(self, ctx, error):
		await ctx.send(error)
		print(error)
		raise error
            
def setup(bot):
	bot.add_cog(EightballCom(bot))
	print('8Ball Commands Loaded Successfully!')
