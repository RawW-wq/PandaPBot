import discord,random,aiohttp,requests
from discord.ext import commands

class NSFW(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def femdom(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/femdom")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def classic(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/classic")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)

	@commands.command()
	async def les(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/les")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def hololewd(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/hololewd")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def lewdk(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/lewdk")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def keta(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/keta")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def feetg(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/feetg")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def nsfw_neko_gif(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def eroyuri(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/eroyuri")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def pussy_jpg(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/pussy_jpg")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)

	@commands.command()
	async def cum_jpg(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/cum_jpg")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def pussy(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/pussy")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def lewdkemo(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/lewdkemo")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)

	@commands.command()
	async def lewd(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/lewd")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def cum(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/cum")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def spank(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/spank")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def kuni(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/kuni")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)

	@commands.command()
	async def boobs(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/boobs")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)

	@commands.command()
	async def feet(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/feet")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def solog(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/solog")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def holo(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/holo")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def bj(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/bj")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def yuri(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/yuri")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def trap(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/trap")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)

	@commands.command()
	async def anal(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/anal")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
	
	@commands.command()
	async def blowjob(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/eroyuri")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def holoero(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/holoero")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)

	@commands.command()
	async def futanari(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/futanari")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def ero(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/ero")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)

	@commands.command()
	async def pwankg(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/pwankg")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def eron(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/eron")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)
			
	@commands.command()
	async def erokemo(self, ctx): 
		if ctx.channel.is_nsfw():
			r = requests.get("https://nekos.life/api/v2/img/erokemo")
			res = r.json()
			em = discord.Embed(color=random.randint(0, 0xFFFFFF))
			em.set_image(url=res['url'])
			em.set_footer(text= f"requested by {ctx.author.name}", icon_url= ctx.author.avatar_url)
			await ctx.send(embed=em)   
		else:
			no=discord.Embed(title='Not an nsfw channel', description='Get your **horny** ass into an nsfw🔞 channel or mark this one as such', color = 0x3498DB)
			no.set_image(url='https://i.imgur.com/SiLd6Nj.gif')
			await ctx.send(embed = no)


def setup(bot):
	bot.add_cog(NSFW(bot))
	print('🔞 NSFW Commands Loaded Successfully!')
