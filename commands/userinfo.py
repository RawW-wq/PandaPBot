import discord
from discord.ext import commands

class UserinfoCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases = ['whois','user'])
	async def userinfo(self, ctx, member:discord.Member=None):
		member = ctx.message.author if not member else member
		guild = ctx.guild
		name = f"{member.name}#{member.discriminator}"
		status = member.status
		joined = member.joined_at
		role = member.roles
		roles = member.roles
		memberid = member.id
		created = member.created_at
		memberav = member.avatar_url
		embed = discord.Embed(title=f"User Info {guild.name}", description=f'{member.mention}', colour=0x6FB900)
		embed.set_author(name = f'{member}', icon_url = f'{memberav}')
		embed.set_thumbnail(url = f'{memberav}')
		embed.add_field(name="Created at", value=f"{created}", inline = True)
		embed.add_field(name="Joined at", value=f"{joined}", inline = True)
		embed.add_field(name="Roles [{}]".format(len(member.roles)-1), value = " ".join([role.mention for role in roles]), inline=False)
		embed.set_footer(text = f'User ID : {memberid}', icon_url = f'{memberav}')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(UserinfoCom(bot))
	print('User Info Command Loaded Successfully!')
