import discord
import os 
import asyncio
import datetime
import random
from discord import user
from discord.ext import commands
from discord.utils import get
from random import randint
import sys, re
from javascript import require, On, Once, AsyncTask, once, off
mineflayer = require('mineflayer', "latest")
pathfinder = require('mineflayer-pathfinder')

BOT_USERNAME = 'afarts33@yahoo.com'

bot = mineflayer.createBot({
  'host': 'mc.hypixel.net',
  'port': 25565,
  'username': BOT_USERNAME,
  'password': 'afarts33',
  'hideErrors': False
})

bot.loadPlugin(pathfinder.pathfinder)
print("Started mineflayer")

once(bot, 'login')
print("i loggged in ")


@On(bot, 'chat',)

def handleMsg(this, user, rawMessage , *args):
  rawMessage == rawMessage
  user == user 
  this = this 
  print(f' {user}: {rawMessage}')


@On(bot, "chat")
def handle(this, username, message, *args):
    if message.startswith("You are AFK. Move around to return from AFK."):
      bot.chat('/l')

users_list = []
intents = discord.Intents().all()
bot = commands.Bot(command_prefix = "$")
@bot.event
async def on_ready():
  this, user, rawMessage,*args = handleMsg()    
  print('Online')
  channel = bot.get_channel(901491654500946000)
  await channel.send(f' {user}: {rawMessage}')




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



bot.run('OTAxNjM0NTMzMTM1MzUxODI5.YXSumA.05K0FiYTS8lFeOaZaZM5QgS_6go')
  
