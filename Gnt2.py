import discord
import os 
import asyncio
import datetime
import random
from discord.ext import commands
from discord.utils import get
from random import randint

users_list = []
intents = discord.Intents().all()
bot = commands.Bot(command_prefix = "$")
@bot.event
async def on_ready():    
  print('Online')
@bot.command()
@commands.has_role("[OwOner]")
async def winner(ctx):
  file_users = open("myfile.txt", "r", '\n')
  message = await ctx.send("Chossing winner...")
  await asyncio.sleep(5)
  await message.edit(file_users)
@bot.command()
@commands.has_role("[OwOner]")
async def offline(ctx):
    channel = bot.get_channel(826097423088353280)
    message = await channel.send("Going offline...")
    await asyncio.sleep(5)
    await message.edit(content = "Offline 🔴")

@bot.command()
async def test(ctx):
    print('Nha')
    await ctx.send('Working')

@bot.command()
async def thiscommandliterallydoesnothingbutpingyou(ctx):
  await ctx.send(f'{ctx.message.author.mention}' )
@bot.command()
@commands.has_role("[Staff]")
async def mute(ctx, member: discord.Member):
    role_muted = discord.utils.get(ctx.guild.roles, name='muted')
    await member.add_roles(role_muted)
    await ctx.send(f'{member.mention} have been muted  ')

@bot.command()
@commands.has_role("[Staff]")
async def unmute(ctx, member: discord.Member):
    role_muted = discord.utils.get(ctx.guild.roles, name='muted')
    await member.remove_roles(role_muted)
    await ctx.send(f'{member.mention} have been unmuted  ')
@bot.command()
@commands.has_role("[OwOner]")
async def inv(ctx, member: discord.Member):
  embedVar = discord.Embed(title="Welcome to guild not take, react on the check mark to join the guild ", color=0x00ff020)
  embedVar.add_field(name="Note: ", value="``` welcome to Guild Name Taken! (If you're a Ninjago fan you get extra perks!  ``` ", inline=True )
  message = await ctx.send(embed=embedVar)
  await message.add_reaction("✅")

@bot.command()
async def msg(ctx, *,  arg):
  print(f'{ctx.message.author}', arg)
  await ctx.send(f'{ctx.message.author.mention, arg}, has been sent to the developers of this bot')

@bot.command()
async def suggest(ctx, *, arg):
  embedVar = discord.Embed(color=0x00ff00)
  embedVar.add_field(name="suggestion", value=arg)
  channel = bot.get_channel(826121781202255872)
  message = await channel.send(embed=embedVar)
  await channel.send("suggested by:"f'{ctx.message.author.mention}',arg) 
  await message.add_reaction("✅")
  await message.add_reaction("❎")



@bot.command()
async def poll(ctx,*, arg):
  message = await ctx.send(arg)
  await message.add_reaction("✅")
  await message.add_reaction("❎")

@bot.command()
async def soon(ctx):
    embedVar = discord.Embed(color=0x11ff00)
    embedVar.add_field(name="coming soon:", value="Coming soon:tm:")
    await ctx.send(embed=embedVar)
@bot.command()
async def applyguild(ctx, *, arg):
    channel = bot.get_channel(826121781202255872)
    embedVar = discord.Embed(name="New application",value=" ")
    embedVar.add_field(name="discord id:"f'{ctx.message.author.mention}', value="weight:"f'{arg}')
    await ctx.send('weight has been recorded, staff will dm you within 24 hours')
    await channel.send(embed=embedVar)
    message = await channel.send(embed=embedVar)
    await message.add_reaction("✅")
    await message.add_reaction("❎")

@bot.command()
async def apply(ctx):
    await ctx.send("Please use $applyguild(weight + sky.shiyyu.moe link) to apply for this guild ")

@bot.command()
async def dmtest(ctx):
    await ctx.author.send("this is a test Ps. this is a future command that will slide crap into your dm's")
@bot.command()
async def dm(ctx, member: discord.Member, *,arg):
    await member.send(arg)
@bot.command()
async def time(ctx):
    time = datetime.datetime.utcnow()
    await ctx.send(time)
@bot.command()
async def kick(ctx, member: discord.Member, * , arg):
  reason = arg
  await member.kick(reason=reason)
  await ctx.send(f'User {member.mention} has kicked.')
  await member.send(arg)

@bot.command()
async def ban(ctx, member: discord.Member, *, arg):
  reason = arg 
  await member.ban(reason=reason)
  await member.send(arg)
  await ctx.send(f'user{member.mention} has been wiped(for now).')

@bot.command()
async def nw(ctx,*,arg):
  await ctx.send(f'{ctx.author.mention}HA, April fools :D')
@bot.command()
async def upload(ctx, *, arg):
  channel = bot.get_channel(826481401565020160)
  await channel.send(f'Crit posed new content: {arg}')
@bot.command()
async def critplayspit(ctx):
  await ctx.send("You won $1,000,000 skyblock coins dm @ethanoly#1940 to get ur coins")
@bot.command()
async def bzflip(ctx):
  embedVar = discord.Embed(name="Best Flips",value=" ")
  embedVar.add_field(name="Enchanted iron blocks(craft)",value="Foul flesh(buy order),enchanted cobble stone(buy order), enchanted lava bucket(buy order)")
  await ctx.send("this feature is down, will be advanced in the future")
@bot.command()
async def ahflip(ctx):
  await ctx.send("coming soon:tm:")
@bot.command()
async def embed(ctx):
  channel = bot.get_channel(838058407734935592)

  embedVar = discord.Embed(name="Slayer",value="‏‏‎‏‏‎ ‎",color=0x00FF00)
  embedVar.add_field(name="Revenants",value="‏‏‎‎‎‎ what if i just type something very long here so that it will extent the size of this embed", inline=False)
  embedVar.add_field(name=" ‎‎",value="‏‏‎‏‏‎**Tier 5**", inline=True)
  embedVar.add_field(name="Regular",value="10k per boss", inline=False)
  embedVar.add_field(name="150mf:",value="+30k", inline=True)
  embedVar.add_field(name="140mf",value="+20k", inline=False)
  embedVar.add_field(name="130mf",value="+10k", inline=False)
  embedVar.add_field(name="‎‎‎‎‏‏‎Tier 4‎",value=" ‎",inline=False)  
  embedVar.add_field(name="EXP",value="5k per boss ", inline=False)
  embedVar.add_field(name="150mf:",value="+30k per boss", inline=False)
  embedVar.add_field(name="140mf",value="20k per boss", inline=False)
  embedVar.add_field(name="130mf",value="+10k per boss", inline=False)
  embedVar.add_field(name="‏‏‎Svens",value="  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎", inline=False)
  embedVar.add_field(name="Tier 4 ",value=" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎", inline=False)
  embedVar.add_field(name="140mf",value="50k per boss", inline=False)
  embedVar.add_field(name="130mf",value="40k per boss", inline=False)
  embedVar.add_field(name="EXP",value="30k per boss", inline=False)
  embedVar.add_field(name="Tier 3",value="  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎", inline=False)
  embedVar.add_field(name="EXP",value="10k per boss", inline=False)
  embedVar.add_field(name="‏‏‎Taratulas",value="  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎", inline=False)
  embedVar.add_field(name="Tier 4's",value="  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎", inline=False)
  embedVar.add_field(name="130mf:",value="30k per boss", inline=False)
  embedVar.add_field(name="120mf:",value="20k per boss", inline=False)
  embedVar.add_field(name="EXP",value="10k per boss" )
  embedVar.add_field(name="Tier 3",value=" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎", inline=False)
  embedVar.add_field(name="130mf:",value="20k per boss", inline=False)
  embedVar.add_field(name="120mf:",value="10k per boss", inline=False)
  embedVar.add_field(name="EXP",value="5k per boss", inline=False)
  embedVar.add_field(name="Barels Slayer",value=" basically you donate. open a support ticket to donte this will help us.  ‎")

@bot.command()
async def alexisadumbbitch(ctx):
  await ctx.send("Alright, if you found this command in the help menu, then get lost. If you just typed randomly, you are a fucking legend")
@bot.command()
async def waitethanhowmuchexperienceuhaveincode(ctx):
  await ctx.send("you tell me ")
@bot.command()
async def cashmoney(ctx):
  channel = bot.get_channel(869340112046141490)
  cash = random.randint(0,1000)
  embedVar = discord.Embed(name=" ",value=" ",color=0xFF0000)
  embedVar.add_field(name="You did not win " , value="**Your number:**"f'{cash}', inline=True)
  await channel.send(f'{ctx.message.author.mention}', embed=embedVar)
  if cash==100:
    rle = ctx.guild.get_role(768454051926769715)
    await ctx.send(rle.mention)
    await ctx.send(f'{ctx.message.author.mention}You have won the 10m')
@bot.command()
async def pingstaff(ctx):
  rle = ctx.guild.get_role(768454051926769715)
  await ctx.send(rle.mention)
@bot.command()
async def cm(ctx):
  channel = bot.get_channel(869340112046141490)
  cash = random.randint(0,5647)
  embedVar = discord.Embed(name="You did not win ",value=" ",color=0xFF0000)
  embedVar.add_field(name="You did not win" , value="**Your number:**"f'{cash}', inline=False)
  await channel.send(f'{ctx.message.author.mention}', embed=embedVar)
  if cash==2:
    rle = ctx.guild.get_role(768454051926769715)
    embedVar = discord.Embed(name="You did not win ",value=" ",color=0x00ff00)
    embedVar.add_field(name="You Won the grand prix of 5m(passive giveway)" , value="**Your number:**"f'{cash}', inline=False)
    await ctx.send(f'{rle.mention,ctx.message.author.mention}', embed=embedVar)
  elif cash==69:
    rle = ctx.guild.get_role(768454051926769715)
    embedVar = discord.Embed(name="You did not win ",value=" ",color=0x00ff00) 
    embedVar.add_field(name="You Won" , value="**Your number**"f'{cash}', inline=False)
    embedVar.add_field(name="alright here is the deal, you got 69 so we will give you 1m, ya know just for getting it.")
    await ctx.send(f'{rle.mention,ctx.message.author.mention}', embed=embedVar)
@bot.command()
@commands.has_role("{VIP]")
async def wow(ctx):
  cash = random.randint(0,2003)
  embedVar = discord.Embed(name=" ",value=" ",color=0xFF0000)
  embedVar.add_field(name="Your number: " , value="Your number:"f'{cash}', inline=True)
  await ctx.send(f'{ctx.message.author.mention}', embed=embedVar)

  #done :D
bot.run('Nzk2ODY4NDU4MDgzMTIzMjUx.X_eLlQ.yiNrMIm30hIIk7ry9dDN5th66LM')
