import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import os,traceback,requests,time,asyncio

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.command()
async def a(ctx):
	while True:
		url = "https://rmt.club/post_list?title=5121&search_word=&deal_type_id=1&price_lower=&price_upper=&is_search=1&sort=update&deal_account_id=0"
		res = requests.get(url).text
		soup = BeautifulSoup(res, 'html.parser')
		for hoge in soup.find_all('div', class_='post-list-row'):
			for h in soup.find_all('div', class_='title')[0:5]:
				if "リゼロ" in h.get_text():await ctx.send(f"{ctx.message.author.mention} "+h.get_text()+'\nhttps://rmt.club/post_list?title=5121&search_word=&deal_type_id=1&price_lower=&price_upper=&is_search=1&sort=update&deal_account_id=0')
				else:await ctx.send(f"{ctx.message.author.mention} ありませんでした！")
		time.sleep(21600)

bot.run("Njg1Njc2NzQ3MTczMTM0MzM3.XuX1gQ.t-1P0fcYWi3vKijWMYgVf2HOcMU")
