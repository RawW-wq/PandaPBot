import discord,praw,random
from discord.ext import commands

reddit = praw.Reddit(client_id='oC6A-NcgrcDc9Q',
					 client_secret='XbIp2Goz5ihaNcInTp5caQrCniA',
					 user_agent='randombotlmao')

class MemeCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def meme(self, ctx):
		memes_submissions = reddit.subreddit('memes').hot()
		post_to_pick = random.randint(1, 10)
		for i in range(0, post_to_pick):
			submission = next(x for x in memes_submissions if not x.stickied)
	
		guild = ctx.guild
		guildav = guild.icon_url
		embed = discord.Embed(title = f'{guild.name} Memey', description = 'Memes from'+' [r/memes](https://www.reddit.com/r/memes)', colour = 0x6FB900)
		embed.set_image(url = submission.url)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(MemeCom(bot))
	print('Meme Command Loaded Successfully!')
