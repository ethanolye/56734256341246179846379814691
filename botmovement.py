
from asyncio.tasks import wait
from inspect import BlockFinder
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
  'host': 'doodsmps.minehut.gg',
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
RANGE_GOAL = 0.001


@On(mcbot, "chat")
def handle( username, message, *args):
    if message.startswith("You are AFK. Move around to return from AFK."):
      mcbot.chat('/l') 
@On(mcbot, 'chat')
def breakListener(this, sender, message, *args):
  if sender and (sender != BOT_USERNAME):
    if 'break' in message:
      pos = mcbot.entity.position.offset(0, -1, 0)
      blockUnder = mcbot.blockAt(pos)
      if mcbot.canDigBlock(blockUnder):
        print(f"I'm breaking the '{blockUnder.name}' block underneath")
        # The start=True parameter means to immediately invoke the function underneath
        # If left blank, you can start it with the `start()` function later on.
        try:
          @AsyncTask(start=True)
          def break_block(task):
            mcbot.dig(blockUnder)
          mcbot.chat('I started digging!')
        except Exception as e:
          print(f"I had an error {e}")
      else:
        print(f"I can't break the '{blockUnder.name}' block underneath")

@On(mcbot, 'chat')
def handleMsg(this, sender, message, *args):
  if sender and (sender != BOT_USERNAME):
    if 'come' in message:
      player = mcbot.players[sender]
      target = player.entity
      bottom = mcbot.entity
      if not target:
        return
      pos = target.position
      pos2 = bottom.position
      mcbot.pathfinder.setMovements(movements)
      mcbot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, RANGE_GOAL))
      po = pos.x
      b = round(pos.y, 0)
      c = round(pos.z, 0)
      d = round(pos2.x,0)
      e = round(pos2.y,0)
      f = round(pos2.z,0)
      

      
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
  
bot.run('OTAxNjM0NTMzMTM1MzUxODI5.YXSumA.E5DwGHzKc-_uzJbPH9-7eQMl08k')
  
