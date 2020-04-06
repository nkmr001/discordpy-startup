from discord.ext import commands
import random
import os
import traceback
import requests
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
pong = random.randrange(10)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send(pong)
    
@bot.command()
async def corona(ctx):
    url = "https://japan-cov-19.now.sh/"
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    hoge = soup.find_all('div', class_='brief-item')
    hogehoge = [for h in soup.find_all('li', class_='brief-item__title')]
    await ctx.send(hogehoge[0:4:-1])

bot.run(token)
