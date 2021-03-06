from aiohttp import ClientSession

import discord, keep_alive, config

from discord.ext import commands as coms

from flask import Flask

from threading import Thread

app = Flask('')

@app.route('/')

def main():

    return "Thanks for support my channel - Zac"

def run():

    app.run(host="0.0.0.0", port=8080)

def keep_alive():

    server = Thread(target=run)

    server.start()

bot = coms.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event

async def on_ready():

  await bot.change_presence(activity=discord.Game(name="Made by ȥαƈ#0249")) #If you're going to change the stats. Please leave these letters here just to credit me.
  
  print("Ready!")

  print(f"Website: {config.Website},")

  print(f"First channel id: {config.CHANNELID1},")
  
  print(f"Second channel id: {config.CHANNELID2}")

@bot.event

async def on_message(msg):
    
  for guild in bot.guilds:

    print(f"{guild.name}")

    if msg.author not in guild.members: 

      return

  channel1 = await bot.fetch_channel(config.CHANNELID1)

  channel2 = await bot.fetch_channel(config.CHANNELID2)
  
  if msg.channel == channel1:
 
    async with ClientSession() as session:
      
          webhook2 = discord.Webhook.from_url(config.WEBHOOK_URL2, adapter=discord.AsyncWebhookAdapter(session))

          await webhook2.send(content=f"{msg.content}", username=msg.author.name, avatar_url=msg.author.avatar_url)

  elif msg.channel == channel2: 

    async with ClientSession() as session:
      
          webhook1 = discord.Webhook.from_url(config.WEBHOOK_URL1, adapter=discord.AsyncWebhookAdapter(session))

          await webhook1.send(content=f"{msg.content}", username=msg.author.name, avatar_url=msg.author.avatar_url)

if config.Website == 'true':

  keep_alive()

bot.run(config.token)
