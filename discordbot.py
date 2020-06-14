import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import os,traceback,requests,time,asyncio

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']
bot.remove_command('help')

with_you = ["256433255723565057"]

def check_with(ctx):
	return ctx.message.author.id in with_you

@bot.command()
async def スタート(ctx):
#@commands.check(check_with)
	url = "https://rmt.club/post_list?title=5121&search_word=&deal_type_id=1&price_lower=&price_upper=&is_search=1&sort=update&deal_account_id=0"
	res = requests.get(url).text
	soup = BeautifulSoup(res, 'html.parser')
	for hoge in soup.find_all('div', class_='post-list-row'):
		for h in soup.find_all('div', class_='title')[0:3]:
			if "雪ミク" in h.get_text():
				await ctx.send(h.get_text()+'\nhttps://rmt.club/post_list?title=5121&search_word=&deal_type_id=1&price_lower=&price_upper=&is_search=1&sort=update&deal_account_id=0')

bot.run(token)
