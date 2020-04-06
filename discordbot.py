from discord.ext import commands
import random
import os
import traceback
import requests
from bs4 import BeautifulSoup
import time

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
async def bio(ctx):
    await ctx.send("日本国内の感染者情報を最新５件表示します")
    url = "https://japan-cov-19.now.sh/"
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    hoge = soup.find_all('div', class_='brief-item')
    for h in soup.find_all('li', class_='brief-item__title')[0:5]:
        await ctx.send(h.get_text())
        time.sleep(1)
 
@bot.command()
async def atari(ctx):
    await ctx.send("攻撃倍率 1.0\n防御倍率1.0\n体力倍率1.0\nロール:スプリンター\n現環境で強いか否か")
    
bot.run(token)
