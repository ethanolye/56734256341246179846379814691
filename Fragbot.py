
from asyncio.tasks import wait
from itertools import repeat
import discord
import os 
import asyncio
import datetime
import time 
import random
import re
import threading
from discord import user
from discord import message
from discord.ext import commands
from discord.utils import get
from random import randint
from types import coroutine
from time import sleep 
import sys, re
from javascript import require, On, Once, AsyncTask, once, off
mineflayer = require('mineflayer', "latest")
pathfinder = require('mineflayer-pathfinder')
users_list = []
intents = discord.Intents().all()
bot = commands.Bot(command_prefix = "$")
pattern = r'^[a-zA-z0-9$]*'

BOT_USERNAME = 'afarts33@yahoo.com'

mcbot = mineflayer.createBot({
  'host': 'mc.hypixel.net',
  'port': 25565,
  'username': BOT_USERNAME,
  'password': 'afarts33',
  'hideErrors': False
})


once(mcbot, 'login')
print("i loggged in ")
time.sleep(2)
mcbot.chat('/play sb')

pathfinder = require('mineflayer-pathfinder')
mcbot.loadPlugin(pathfinder.pathfinder)
# Create a new minecraft-data instance with the bot's version
mcData = require('minecraft-data')(mcbot.version)
# Create a new movements class
movements = pathfinder.Movements(mcbot, mcData)
# How far to be fromt the goal
RANGE_GOAL = 1

loop = asyncio.new_event_loop()

@On(mcbot,'messagestr')
def handleMsg(this,message,messagePosition,*_):
  if "robpyle13" in message:
    return
  if ":" in message:
      x = datetime.datetime.now()
      print(message)
      file_users = open("Ingametext.txt", "a")
      if "❤" in message: 
        pass
      if "◆" in message:
        pass 
      if "⭐" in message:
        pass 
      
      file_users.writelines(f'{x.strftime("%c")} : {message}\n')
      file_users.close()
  if message.startswith("You were spawned in Limbo."):
    mcbot.chat("/l ")
    sleep(2.0)
    mcbot.chat("/play sb")
  if "party" and ">" and  "bruyhrew" in message:
    x = datetime.datetime.now()
    mcbot.chat(f'/pc {x.strftime("%c")}')
  if "limbo" in message:
    x = datetime.datetime.now()
    mcbot.chat("/l")
    print(f'{x.strftime("%c")}: {message}')
  if "You are currently connected to server" in message:
    print(message)
@On(mcbot,'messagestr')
def handleMsg(this,message,messagePosition,*_):
  if "robpyle13" in message:
    return
  if "invited" in message:

    u = re.search(r'](.*?)has', message).group(1)
    x = datetime.datetime.now()
    ra = random.randint(0,9999999)
    print(f'{x.strftime("%c")} {u} ID:{ra}')
    mcbot.chat(f'/p accept{u}')
    sleep(1)
    mcbot.chat(f'/pc Thanks for using this bot ID:{ra}')
    sleep(0.5)
    mcbot.chat("/pc Thanks for using this bot")
    sleep(3)
    mcbot.chat("/p leave")
    file_users = open("Frag-people.txt", "a")
    file_users.writelines(f'{x.strftime("%c")} Name:{u} ID:{ra}\n')
    file_users.close()

loop = asyncio.get_event_loop()
@On(mcbot,'chat')
def handleMsg(this,user,message,*args):
  if "robpyle13" in message:
    return
  channel = bot.get_channel(911054894327283732)
  embedVar = discord.Embed(name=f'message ',value=f'message',color=0x66ffcc)
  embedVar.add_field(name=f'{user}',value=f'{message}', inline=True)
  asyncio.run_coroutine_threadsafe(channel.send(embed=embedVar),loop)
@On(mcbot,'chat')
def handleMsg(this,user,message,*args):
  x = ['selling', 'SELLING','Selling','ah','Ah','AH','buying','BUYING']
  gotmatch = False
  for y in x:
    match = re.search(y, message)
    if match:
        gotmatch = True
        break
  if gotmatch:
    channel = bot.get_channel(912457100477726750)
    embedVar = discord.Embed(name=f'message ',value=f'message',color=0x66ffcc)
    embedVar.add_field(name=f'{user}',value=f'{message}', inline=True)
    asyncio.run_coroutine_threadsafe(channel.send(embed=embedVar),loop)


@On(mcbot, 'chat')
def handleMsg(this, sender, message, *args):
  if sender and (sender != BOT_USERNAME):
    if '34578324' in message:
      o = re.search(r']\s(.*?):',message).group(1)
      player = mcbot.players[o]
      target = player.entity
      if not target:
        mcbot.chat("/pc no see you")
        return
      pos = target.position
      mcbot.pathfinder.setMovements(movements)
      mcbot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, RANGE_GOAL))
    if 'stop' in message:
      off(mcbot, 'chat', handleMsg)
  
@On(mcbot, "chat")
def handle( username, message, *args):
    if message.startswith("You are AFK. Move around to return from AFK."):
      mcbot.chat('/l') 
@bot.command()
async def ree(ctx):
  mcbot.chat('hello this is poggers')

@bot.command()
async def dm(ctx, member: discord.Member, *,arg):
    await member.send(arg)

@bot.command()
async def time(ctx):
    time = datetime.datetime.utcnow()
    await ctx.send(time)

@bot.command()
async def thiscommandliterallydoesnothingbutpingyou(ctx):
  await ctx.send(f'{ctx.message.author.mention}' )
@bot.command()
async def say(ctx,*,arg):
  mcbot.chat(f'{arg}')
  

@bot.command()
async def dmtest(ctx, member: discord.Member):
  await member.send("")
@bot.command()
@commands.has_role("[OwOner]")
async def kick(ctx, member: discord.Member, * , arg):
  reason = arg
  await member.kick(reason=reason)
  await ctx.send(f'User {member.mention} has kicked.')
  await member.send(arg)

@bot.command()
@commands.has_role("[OwOner]")
async def ban(ctx, member: discord.Member, *, arg):
  reason = arg 
  await member.ban(reason=reason)
  await member.send(arg)
  await ctx.send(f'user{member.mention} has been wiped(for now).')
  
bot.run('OTAxNjM0NTMzMTM1MzUxODI5.YXSumA.0UZ31LLQycdqLdgQ6BvjapRBwzg')
  
