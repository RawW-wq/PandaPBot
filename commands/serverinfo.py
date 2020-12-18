import discord
from discord.ext import commands

class ServerinfoCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases = ['sinfo']) #ready
	async def serverinfo(self, ctx):
		guild = ctx.guild
		embed = discord.Embed(title=f"Server Info", colour=0x6FB900)
		embed.set_author(name = f'{guild.name}', icon_url = f'{guild.icon_url}')
		embed.set_thumbnail(url = f'{guild.icon_url}')
		embed.add_field(name = 'Server Members', value = f'{guild.member_count}', inline = False)
		embed.add_field(name = 'Server Owner', value = f'{guild.owner}', inline = False)
		embed.add_field(name = 'Created At', value = f'{guild.created_at}', inline = False)
		embed.add_field(name = 'Boost Level', value = f'{guild.premium_tier}', inline = False)
		embed.add_field(name = 'Region', value = f'{guild.region}', inline = True)
		
		await ctx.send(embed = embed)

def setup(bot):
	bot.add_cog(ServerinfoCom(bot))
	print('Server Info Command Loaded Successfully!')
