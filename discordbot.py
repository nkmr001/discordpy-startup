import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import random,os,traceback,requests,time,asyncio,sqlite3

cmps = sqlite3.connect("cmps.db")
c = cmps.cursor()
bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']
bot.remove_command('help')

def DBclose():
	c.commit()
	c.close()

Notice_txt = None
owner = ["263614623238848522"]
roll_list = ["アタッカー","ガンナー","タンク","スプリンター"]
Reg_text = ["""
主に使用するロール:
デッキレベル:
実力:
通話が可能か:
一言:
"""]

def check_owner(ctx):
	return ctx.message.author.id in owner

c.execute("""CREATE TABLE users
 (ユーザーID text,
 名前 text,
 使用キャラクター text,
 デッキレベル INTEGER,
 実力 text,
 通話 text,
 一言 text
 );""")

c.execute("""CREATE TABLE rolls
 (name text,
 roll text,
 info text);""")

DBclose()

###################オーナーコマンド####################

@bot.command()
@commands.check(check_owner)
async def Nedit(ctx, N=None):
	global Notice_txt
	Notice_txt = N
	await ctx.send(N+"\nをお知らせを編集しました")

@bot.command(pass_context=True, name="kick")
@commands.check(check_owner)
async def kick(ctx, member: discord.Member, *, reason=None):
	try:await member.kick(reason=reason)
	except:await ctx.send("キックできませんでした。")

@bot.command()
@commands.check(check_owner)
async def addinfo(ctx,chara_name=None,roll_name=None,info_txt=None):
	if chara_name == None or roll_name not in roll_list:await ctx.send("ロールかキャラ名が正しくありません")
	else:
		chara_info = (chara_name,roll_name,info_txt)
		c.execute('insert into rolls (name,roll,info) values (?,?,?)', chara_info)
		DBclose()
		await ctx.send(chara_name+"の情報を追加しました")

@bot.command()
@commands.check(check_owner)
async def editinfo(ctx,chara_name=None,roll_name=None,info_txt=None):
	R_list = [for R in c.execute("select * from rolls where name = chara_name")]
	if chara_name not in R_list:await ctx.send("キャラが登録されていません")
	else:
		c.execute('update rolls set name = chara_name where name == chara_name')
		c.execute('update rolls set roll = roll_name where name == chara_name')
		c.execute('update rolls set info = info_txt where name == chara_name')
		DBclose()
		await ctx.send(chara_name+"の情報を修正しました")

@bot.command()
@commands.check(check_owner)
async def editinfo(ctx,chara_name=None)
	R_list = [for R in c.execute("select * from rolls where name = chara_name")]
	if chara_name not in R_list:await ctx.send("存在していません")
	else:
		c.execute('delete from rolls where name == chara_name')
		DBclose()
		await ctx.send(chara_name+"の情報を削除しました")

#################################################################
#####################メッセージ周り##############################
@bot.event
async def on_message(message):
	if message.content == "!Reg":
			m_id = message.author.id
			channel = message.channel
			await channel.send(Reg_text)
			def check_mes(message):
				return message.author.id == m_id and message.channel == channel or message.content in roll_list and Reg_text
			try:
				mes = await bot.wait_for('message', timeout=300.0, check=check_mes)
			except asyncio.TimeoutError:
				await channel.send("タイムアウトしたよ。最初からやり直してね")
			else:
				mes = mes.content
				if デッキレベルが4以下241以上の場合:
				elif 空欄がある場合:
				elif 既に登録されている場合:
					await channel.send(f"{m_id.mention}様の情報を修正しました")
				else:await channel.send(f"{m_id.mention}様の情報を登録しました")
	if "https://compass.link/fb/" in message.content:
			m_id = message.author.id
			if m_id != 700618658799419512:
				ch = bot.get_channel(701525994908942448)
				cl = message.channel
				room_mes = message.content
				await ch.send(message.author.name+"さんがイベントアリーナのメンバーを募集しています\n"+room_mes[60:119])
				await cl.send("https://discord.gg/knYwFb9\nに貼っておきました")
	if "https://compass.link/ba/" in message.content:
			m_id = message.author.id
			if m_id != 700618658799419512:
				ch = bot.get_channel(701525994908942448)
				cl = message.channel
				room_mes = message.content
				await ch.send(message.author.name+"さんがバトルアリーナのメンバーを募集しています\n"+room_mes[61:94])
				await cl.send("https://discord.gg/knYwFb9\nに貼っておきました")
	if "https://compass.link/cb" in message.content:
			if m_id != 700618658799419512:
				ch = bot.get_channel(701525994908942448)
				cl = message.channel
				room_mes = message.content
				await ch.send(message.author.name+"さんがカスタムバトルのメンバーを募集しています\n"+room_mes[55:100])
				await cl.send("https://discord.gg/knYwFb9\nに貼っておきました")
	if message.content == "!cmps":
		channel = message.channel
		embed = discord.Embed(title="何が知りたいの？",description="知りたいことを書き込んでね")
		embed.add_field(name="アタッカー",value=atk,inline=False)#valueをrollsのアタッカーロールをリストにしたものを入れる
		embed.add_field(name="\nガンナー",value=gun,inline=False)#valueをrollsのガンナーロールをリストにしたものを入れる
		embed.add_field(name="\nスプリンター",value=supri,inline=False)#valueをrollsのスプリンターロールをリストにしたものを入れる
		embed.add_field(name="\nタンク",value=tank,inline=False)#valueをrollsのタンクロールをリストにしたものを入れる
		await channel.send(embed=embed)
		def check(message):
			return message.content in [i for i in compass.keys()] and message.channel == channel　#[i for i in compass.keys()]の部分をrollsからnameで引っ張ってくる
		try:
			msg = await bot.wait_for('message', timeout=30.0, check=check)
		except asyncio.TimeoutError:
			await message.delete()
			await channel.send("タイムアウトしたよ。最初からやり直してね")
		else:
			await channel.send(compass[msg.content].format(msg))
	await bot.process_commands(message)
################################################################
@bot.command()
async def P(ctx):#自分のプロフィールを表示
	m_id = ctx.message.author.id
	if m_id in rireki_text.keys():#ディスコードのIDとusersのIDで探して表示
		await ctx.send(f'{ctx.message.author.mention}さんのプロフィール\n'+rireki_text[m_id])
	else:await ctx.send(f"{ctx.message.author.mention}さんはまだ登録されていません。「！登録」でプロフィールを入力してください")

@bot.command()#プロフィールを検索
async def searchP(ctx, rol=None, level=None):
	if member.id in rireki_text.keys():#usersからデッキレベルorロールで引っ張ってくる
		await ctx.send(f'{member.mention}さんのプロフィールを表示します\n'+rireki_text[member.id])
	else:await ctx.send(f"{member.mention}さんはまだ登録されていません。")

@bot.command()#メンションした人のプロフィール表示
async def MemP(ctx,member: discord.Member):
	if member.id in rireki_text.keys():
		await ctx.send(f'{member.mention}さんのプロフィールを表示します\n'+rireki_text[member.id])
	else:await ctx.send(f"{member.mention}さんはまだ登録されていません。")

@bot.command()
async def Notice(ctx):
	await ctx.send(Notice_txt)

@bot.commad()
async def COVID(ctx):
	await ctx.send("日本国内の感染者情報の最新５件を表示します")
	url = "https://japan-cov-19.now.sh/"
	res = requests.get(url).text
	soup = BeautifulSoup(res, 'html.parser')
	hoge = soup.find_all('div', class_='brief-item')
	for h in soup.find_all('li', class_='brief-item__title')[0:5]:
		await ctx.send(h.get_text())
		time.sleep(1)

@bot.command()
async def URL(ctx):
	await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=685676747173134337&permissions=8&scope=bot\n招待したいサーバーの管理者が操作してください")

@bot.command()
async def ariria(ctx):
	url = "http://ariria.com/"
	res = requests.get(url).text
	soup = BeautifulSoup(res, 'html.parser')
	ariria = soup.find_all('h2',class_= "entry-title",itemprop="headline")
	ari = ariria[1].find("a")
	await ctx.send(ariria[1].get_text()+'\n'+ari.get("href"))

@bot.command()
async def wanted(ctx, about=None, arg=None):
	ch = bot.get_channel(701525994908942448)
	arg = str(arg)
	await ch.send(ctx.message.author.name+"さんのメッセージです")
	test = discord.Embed(title=about,colour=0x1e90ff)
	test.add_field(name="条件", value=f"{arg}", inline=True)
	await ch.send(embed=test)
	await ctx.send("https://discord.gg/knYwFb9\nに募集文を送信しました。")

@bot.command()#rollsから引っ張ってくる
async def ram(stx,ram_txt=None):
	if ram_txt == None:
	if ram_txt == "アタッカー":
	if ram_txt == "ガンナー":
	if ram_txt == "スプリンター":
	if ram_txt == "タンク":
	if ram_txt == "パーティー":

@bot.command()
async def help(ctx):
	embed = discord.Embed(title="マニュアル",description="コマンド見にくくてごめん。",color=0xff0000)
	embed.add_field(name="!Reg",value="",inline=False)
	embed.add_field(name="!cmps",value="",inline=False)
	embed.add_field(name="!ram",value="",inline=False)
	embed.add_field(name="!P",value="",inline=False)
	embed.add_field(name="!Notice",value="",inline=False)
	embed.add_field(name="!URL",value="",inline=False)
	embed.add_field(name="!ariria",value="",inline=False)
	embed.add_field(name="!wanted",value="",inline=False)
	embed.add_field(name="!COVID",value="",inline=False)
	await ctx.send(embed=embed)

bot.run(token)
