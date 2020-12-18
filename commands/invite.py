import discord
from discord.ext import commands

class InviteCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def invite(self, ctx):
		embed = discord.Embed(title = f"Invite PandaP", description = '[Click Here To Invite The Bot](https://discord.com/api/oauth2/authorize?client_id=746076516722409534&permissions=8&scope=bot)\n[Join The Support Server](https://discord.gg/3ngfByHbsR)', color = 0x6FB900)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(InviteCom(bot))
	print('Invite Command Loaded Successfully!')
