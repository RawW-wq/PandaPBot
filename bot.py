import discord
import random
import os
import datetime
import asyncio
import praw
import json
import requests
import aiohttp
import asyncpg
from time import time
from datetime import datetime
from copy import copy
from discord.ext import commands
from discord import Activity, ActivityType
from discord.ext.commands import clean_content
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix=('p!'),case_insensitive=True)

async def startup():
	await bot.wait_until_ready()
	await bot.change_presence(activity=Activity(name=f"PandaP Discord Bot - p!help", type=ActivityType.watching))

bot.loop.create_task(startup())

@bot.event
async def on_ready():
	print('Logged in as : {0}'.format(bot.user))

bot.snipes = {}

@bot.event
async def on_message_delete(message):
  bot.snipes[message.channel.id] = message

@bot.command()  
async def snipe(ctx, *, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  try:
    msg = bot.snipes[channel.id]
  except KeyError:
    return await ctx.send('Nothing to snipe!')
  # one liner, dont complain
  await ctx.send(embed=discord.Embed(description=msg.content, color=msg.author.color).set_author(name=str(msg.author), icon_url=str(msg.author.avatar_url)))

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return
	raise error

@bot.command()
async def support(ctx):
	await ctx.send('https://discord.com/invite/3ngfByHbsR')

bot.remove_command('help')
bot.load_extension('commands.cat')
bot.load_extension('commands.cry')
bot.load_extension('jishaku')
bot.load_extension('commands.dog')
bot.load_extension('commands.fox')
bot.load_extension('commands.hug')
bot.load_extension('commands.kiss')
bot.load_extension('commands.meme')
bot.load_extension('commands.panda')
bot.load_extension('commands.pat')
bot.load_extension('commands.pikachu')
bot.load_extension('commands.reverse')
bot.load_extension('commands.slap')
bot.load_extension('commands.wink')
bot.load_extension('commands.strawpoll')
bot.load_extension('commands.8ball')
bot.load_extension('commands.coinflip')
bot.load_extension('commands.slot')
bot.load_extension('commands.avatar')
bot.load_extension('commands.help')
bot.load_extension('commands.invite')
bot.load_extension('commands.serverinfo')
bot.load_extension('commands.poll')
bot.load_extension('commands.covid')
bot.load_extension('commands.userinfo')
bot.load_extension('commands.nsfw')

@bot.command()
async def ping(ctx):
	embed = discord.Embed(title="Pong",
							colour=discord.colour.Color.blue(),
							timestamp=datetime.utcnow())
	embed.description = ":heartbeat: **Heartbeat** " + str(f"{round(bot.latency * 1000)}ms")
	start = time()
	msg = await ctx.send(embed=embed)
	end = time()
	embed = discord.Embed(title="Pong",
							colour=discord.colour.Color.blue(),
							timestamp=datetime.utcnow())
	embed.description = ":heartbeat: **Heartbeat** " + str(f"{round(bot.latency * 1000)}ms\n:timer: **Response** {(end - start)*1000:,.0f}ms")
	await msg.edit(embed=embed)

bot.launch_time = datetime.utcnow()

@bot.command()
async def uptime(ctx):
	delta_uptime = datetime.utcnow() - bot.launch_time
	hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	await ctx.send(f"Bot is working for : {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'<a:pandapYes:778196006113771581> | Kicked {member.mention}')

@kick.error
async def kick_error(ctx, error):
	if isinstance(error, MissingPermissions):
		await ctx.send("<a:pandapNo:778196006512361472> You don't have ``KICK_MEMBERS`` permission to kick members.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'<a:pandapYes:778196006113771581> | Banned {member.mention}')

@ban.error
async def ban_error(ctx, error):
	if isinstance(error, MissingPermissions):
		await ctx.send("<a:pandapNo:778196006512361472> | You don't have ``BAN_MEMBERS`` permission to ban members.")

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, id: int):
	user = await bot.fetch_user(id)
	await ctx.guild.unban(user)
	await ctx.send(f'<a:pandapYes:778196006113771581> | Unbanned {user.mention}')
	return
        
@unban.error
async def unban_error(ctx, error):
	if isinstance(error, MissingPermissions):
		await ctx.send("<a:pandapNo:778196006512361472> You don't have ``ADMINISTRATOR`` permission to kick members.")
	else:
		await ctx.send(error)	
		print(error)
		raise error
        
@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=100):
	await ctx.channel.purge(limit=amount + 1)
	await ctx.send(f'<a:pandapYes:778196006113771581> | Deleted {amount} messages', delete_after = 2)

@purge.error
async def purge_error(ctx, error):
	if isinstance(error, MissingPermissions):
		await ctx.send("<a:pandapNo:778196006512361472> | You don't have ``MANAGE_MESSAGES`` permission to purge messages.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member : discord.Member, *, reason=None):
	embed = discord.Embed(title='Warned')
	embed.add_field(name='Member warned', value=f'{member}', inline=False)
	embed.add_field(name='Staff Member', value=f'{ctx.author}', inline=False)
	embed.add_field(name='Reason', value=f'{reason}', inline=False)
	await ctx.send(content=None, embed=embed)

@warn.error
async def warn_error(ctx, error):
	if isinstance(error, MissingPermissions):
		await ctx.send("<a:pandapNo:778196006512361472> | You don't have ``MANAGE_MESSAGES`` permission to warn members.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, words=None, *, colour: discord.Color=None):
	if words == None:
		await ctx.send('Whats the name for the role you want to create?\n**Important** *If the role has 2 names use "" before and after the role name!\nExample: /role "New Role"')
	if colour == None:
		guild = ctx.guild
		await guild.create_role(name=words)
		await ctx.send(f'<a:pandapYes:778196006113771581> | The role **{words}** is created successfully!')
	else:
		guild = ctx.guild
		await guild.create_role(colour=colour, name=words)
		await ctx.send(f'<a:pandapYes:778196006113771581> | The role **{words}** with hex color **{colour}** is created successfully!')

@role.error
async def role_error(ctx, error):
	if isinstance(error, MissingPermissions):
		await ctx.send("<a:pandapNo:778196006512361472> | You don't have ``MANAGE_ROLES`` permission to create roles.")
        
bot.run('Your-Token-Here', reconnect = True)