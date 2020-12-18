import discord,random
from discord.ext import commands

class SlotCom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['slots'])
	async def slot(self, ctx):
		emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)

		slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

		if (a == b == c):
			await ctx.send(f"{slotmachine} All matching, you won! 🎉")
		elif (a == b) or (a == c) or (b == c):
			await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
		else:
			await ctx.send(f"{slotmachine} No match, you lost 😢")

def setup(bot):
	bot.add_cog(SlotCom(bot))
	print('Slot Commands Loaded Successfully!')
