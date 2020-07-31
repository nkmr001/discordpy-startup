import discord
from discord.ext import commands
import os,asyncio,sqlite3
from setting import session
from Server import *

bot = commands.Bot(command_prefix='//')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def check(ctx):
	rank = {}
	ch = bot.get_channel(714188878734688287)
	async for message in ch.history(limit=200):
		rea = message.reactions
		c = 0
		for i in rea:
			if i.emoji == '👍':
				c+=int(i.count)*5
			if i.emoji == '👎':
				c+=int(i.count) * -5
			if i.emoji != '👍' and i.emoji != '👎':
				c+=int(i.count)
		rank[message.content] = int(c)
	rank2 = sorted(rank.items(), key=lambda x:x[1],reverse=True)
	print(rank2)
	embed = discord.Embed(title="映画",description=None,color=0xff0000)
	co = 0
	for em in rank2:
		co+=1
		embed.add_field(name=str(co)+'位 '+str(em[1])+'点',value=em[0],inline=False)
	await ctx.send(embed=embed)

@bot.command()
async def reg(ctx):
	ch = ctx.message.channel.id
	g = ctx.message.guild
	D = Dserver()
	D.name = g
	D.id = ch
	session.add(D)  
	session.commit()
	await ctx.send(str(g)+'を登録しました')
	
@bot.command()
async def list(ctx):
	D = session.query(Dserver).all()
	embed = discord.Embed(title="登録サーバーリスト",description=None,color=0xff0000)
	for row in D:
		embed.add_field(name=row.name,value=row.id,inline=False)
	await ctx.send(embed=embed)

bot.run(token)
