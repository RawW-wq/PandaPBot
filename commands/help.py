import discord
from discord.ext import commands

class HelpCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='help', hidden=True)
	async def asd_help(self, ctx, arg=None):
		if ctx.channel.is_nsfw():    
			if arg is None:
				embed = discord.Embed(title = f"PandaP Commands List", description = f'Use every command **only** in this server!\n\u200b', colour = 0x6FB900)
				embed.add_field(name = ':tools: Utils', value = f'``help utils``', inline = True)
				embed.add_field(name = ':joy: Fun', value = f'``help fun``', inline = True)
				embed.add_field(name = ':round_pushpin: Mod', value = f'``help mod``', inline = True)
				embed.add_field(name = ':video_game: Games', value = f'``help games``', inline = True)
				embed.add_field(name = ':underage: NSFW', value = f'``help nsfw``', inline = True)
				await ctx.send(embed = embed)
			if arg == 'utils':
				mainembed = discord.Embed(title = f'PandaP Utils Commands', description = f'``userinfo``, ``serverinfo``, ``avatar``, ``uptime``, ``help``, ``invite``, ``ping``, ``snipe``, ``poll``', colour = 0x6FB900)
				await ctx.send(embed=mainembed)
			if arg == 'fun':
				funembed = discord.Embed(title = f'PandaP Fun Commands', description = f'``reverse``, ``meme``, ``hug``, ``cry``, ``pat``, ``kiss``, ``wink``, ``slap``, ``pikachu``, ``panda``, ``fox``, ``dog``, ``cat``', colour = 0x6FB900)
				await ctx.send(embed=funembed)
			if arg == 'mod':
				modembed = discord.Embed(title = f'PandaP Mod Commands', description = f'``kick``, ``ban``, ``unban``, ``purge``, ``warn``,  ``role``', colour = 0x6FB900)
				await ctx.send(embed=modembed)
			if arg == 'games':
				modembed = discord.Embed(title = f'PandaP Games Commands', description = f'``8ball``, ``slots``, ``coinflip``', colour = 0x6FB900)
				await ctx.send(embed=modembed)
			if arg == 'nsfw':
				modembed = discord.Embed(title = f'PandaP NSFW Commands', description = f'``femdom``, ``classic``, ``les``, ``hololewd``, ``lewdk``, ``keta``, ``feetg``, ``nsfw_neko_gif``, ``eroyuri``, ``pussy_jpg``, ``cum_jpg``, ``pussy``, ``lewdkemo``, ``lewd``, ``cum``, ``spank``, ``kuni``, ``boobs``, ``feet``, ``solog``, ``holo``, ``bj``, ``yuri``, ``trap``, ``anal``, ``blowjob``, ``holoero``, ``futanari``, ``ero``, ``pwankg``, ``eron``, ``erokemo``', colour = 0x6FB900)
				await ctx.send(embed=modembed)
		else:
			if arg is None:
				embed = discord.Embed(title = f"PandaP Commands List", description = f'Use every command **only** in this server!\n\u200b', colour = 0x6FB900)
				embed.add_field(name = ':tools: Utils', value = f'``help utils``', inline = True)
				embed.add_field(name = ':joy: Fun', value = f'``help fun``', inline = True)
				embed.add_field(name = ':round_pushpin: Mod', value = f'``help mod``', inline = True)
				embed.add_field(name = ':video_game: Games', value = f'``help games``', inline = True)
				embed.add_field(name = ':underage: NSFW', value = f'``help nsfw``', inline = True)
				await ctx.send(embed = embed)
			if arg == 'utils':
				mainembed = discord.Embed(title = f'PandaP Utils Commands', description = f'``userinfo``, ``serverinfo``, ``avatar``, ``uptime``, ``help``, ``invite``, ``ping``, ``snipe``, ``poll``', colour = 0x6FB900)
				await ctx.send(embed=mainembed)
			if arg == 'fun':
				funembed = discord.Embed(title = f'PandaP Fun Commands', description = f'``reverse``, ``meme``, ``hug``, ``cry``, ``pat``, ``kiss``, ``wink``, ``slap``, ``pikachu``, ``panda``, ``fox``, ``dog``, ``cat``', colour = 0x6FB900)
				await ctx.send(embed=funembed)
			if arg == 'mod':
				modembed = discord.Embed(title = f'PandaP Mod Commands', description = f'``prefix``, ``kick``, ``ban``, ``unban``, ``purge``, ``warn``,  ``role``', colour = 0x6FB900)
				await ctx.send(embed=modembed)
			if arg == 'games':
				modembed = discord.Embed(title = f'PandaP Games Commands', description = f'``8ball``, ``slots``, ``coinflip``', colour = 0x6FB900)
				await ctx.send(embed=modembed)
			if arg == 'nsfw':
				modembed = discord.Embed(title = f'PandaP NSFW Commands', description = f'``Use This Command In NSFW Channel``', colour = 0x6FB900)
				await ctx.send(embed=modembed)


def setup(bot):
	bot.add_cog(HelpCom(bot))
	print('Help Command Loaded Successfully!')
