import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import os,traceback,requests,time,asyncio

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']
bot.remove_command('help')

@bot.event
async def on_message(message):
	channel = message.channel
	if "リヴァイ弱" in message.content:
		try:
			await bot.kick(message.author.id)
			await channel.send(f"{message.author.id.mention} 立体機動装置を見たことはあるか？")
		except:await channel.send("作戦の本質を見失った...")

bot.run(token)
