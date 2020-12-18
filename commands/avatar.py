import discord
from discord.ext import commands

class AvatarCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def avatar(self, ctx, *, member: discord.Member=None):
		if not member:
			member = ctx.message.author
		userAvatar = member.avatar_url
		await ctx.send(userAvatar)

	@avatar.error
	async def avatar_error(self, ctx, error):
		await ctx.send(error)
		print(error)
		raise error
        
def setup(bot):
	bot.add_cog(AvatarCom(bot))
	print('Avatar Command Loaded Successfully!')
