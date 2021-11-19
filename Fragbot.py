
import discord
import os 
import asyncio
import datetime
import time 
import random
import re 
from discord import user
from discord import message
from discord.ext import commands
from discord.utils import get
from random import randint
from types import coroutine
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
time.sleep(3)
mcbot.chat('/warp home')

loop = asyncio.new_event_loop()
@On(mcbot,'chat')
def messagestr(this,user,toString ,*args):
  print(f'{user}: {toString}')
  channel = bot.get_channel(911054894327283732)
  embedVar = discord.Embed(name=f'message ',value=f'message')
  embedVar.add_field(name=f'{user}',value=f'{toString}', inline=True)
  bot.loop.create_task(channel.send(embed=embedVar))


  
@On(mcbot, "chat")
def handle( username, message, *args):
    if message.startswith("You are AFK. Move around to return from AFK."):
      mcbot.chat('/l')
@On(mcbot, "chat")
def onChat(this,user,message,*args):
  if 'has invited' in message:
    mcbot.chat('yes')



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



bot.run('OTAxNjM0NTMzMTM1MzUxODI5.YXSumA.2ZPjRojMWUZssifymZfki1hktes')
  
