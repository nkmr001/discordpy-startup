import discord
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

@bot.listen()
async def on_message(message):
	await ctx.send("メッセージを削除します")
	await message.delete()

@bot.event
async def on_command_error(ctx, error):
	orig_error = getattr(error, "original", error)
	error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
	await ctx.send(error_msg)
	await ctx.send("すみません、存在しないコマンドです。\n何かあれば作者のDMまでhttps://twitter.com/mimiQ0012")


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
async def 招待URL(ctx):
	await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=685676747173134337&permissions=8&scope=bot\n招待したいサーバーの管理者が操作してください")


@bot.command()
async def ヘルプ(ctx):
	await ctx.send("/キャラ名でそのキャラの相性の良いキャラと有利対面、不利対面を出します。\n対面については全てタイマンを想定しています。\n耐久型キャラクターのタイマンは倒されやすいかどうかを書いています。\nおすすめカードと立ち回りについては\nhttps://twitter.com/compass_AG\nの記事を引用しています。")


@bot.command()
async def アタリ(ctx):
	await ctx.send("アタリの情報※HS発動時のみ記載\n\n組んで相性の良いキャラ\n・マルコス＆リリカ\n・ディズィー\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・全てのキャラに有利\n\n不利対面\n①貫通\n②毒、サイレント、スタンなどの状態異常\n③ダメカ破壊\n④防御UP中に防御ダウン\n⑤カードキャンセル\n上記のものどれか一つでもまともに食らえば不利になる。\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/229151#link05")


@bot.command()
async def ジャスティス(ctx):
	await ctx.send("ジャスティスの情報\n\n組んで相性の良いキャラ\n・ポロロッチョ\n・スタン持ち\n\n有利、不利対面のキャラ\n・相手にスタンと貫通がなければ有利、あれば不利\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/232405#link05")


@bot.command()
async def リリカ(ctx):
	await ctx.send("リリカの情報\n\n組んで相性の良いキャラ\n・マルコス\n・アタリ\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・自分より射程の短いガンナー\n・ソーン\n\n不利対面のキャラ\n・足の速いアタッカー\n・ギルガメッシュ\n・攻撃寄りスプリンター\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/230284#link05")


@bot.command()
async def ノホ(ctx):
	await ctx.send("ノホの情報\n\n組んで相性の良いキャラ\n・ディズィー\n・トマス\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・体力倍率が0.85以下のキャラほぼ全て(マジスク＆ゆらら前提)\n\n不利対面のキャラ\n・ギルガメッシュ\n・グスタフ\n・きらら\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/232243#link05")


@bot.command()
async def 忠臣(ctx):
	await ctx.send("忠臣の情報\n\n組んで相性の良いキャラ\n・射程の長いガンナー\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・体力倍率0.8以下のキャラ\n\n不利対面のキャラ\n・自分より足が速いキャラ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/231602#link05")


@bot.command()
async def ジャンヌ(ctx):
	await ctx.send("ジャンヌの情報\n\n組んで相性の良いキャラ\n・ポロロッチョ\n・デルミン\n\n耐えやすい対面\n・サーティーン\n・ノホ\n・リリカ\n\n耐え難い対面\n・オカリン\n・ルチアーノ\n・忠臣\n・イスタカ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/229854#link05")

@bot.command()
async def ボイドール(ctx):
	await ctx.send("ボイドールの情報\n\n組んで相性の良いキャラ\n・トマス\n・ボイドの型によって幅広いアタッカー、ガンナーと組みやすい\n\n耐え難い対面\n・お母さん入りガンナー\n・マジスク&貫通持ち\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/231086#link05")

@bot.command()
async def マルコス(ctx):
	await ctx.send("マルコスの情報\n\n組んで相性の良いキャラ\n・リリカ\n・アタリ\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・枝でのカードキャンセルが成功すればほぼ全キャラ\n\n不利対面のキャラ(HSゲージが溜まっていれば対処可)\n・周囲カノーネ持ち\n・マジスク＆ゆらら持ち\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/229810#link05")

@bot.command()
async def ルチアーノ(ctx):
	await ctx.send("ルチアーノの情報\n\n組んで相性の良いキャラ\n・カノーネ持ちキャラクター全般\n・周囲の発動がが速いキャラクター\n\n有利対面のキャラ\n・ディーバのみアタッカー全般\n\n不利対面のキャラ\n・マルコス\n・デルミン\n・自分より射程が長いガンナー\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/232197#link05")

@bot.command()
async def まとい(ctx):
	await ctx.send("まといの情報\n\n組んで相性の良いキャラ\n・ヴィオレッタ\n・フルカノアタッカー\n\n有利対面のキャラ\n・ディズィー\n・ソーン\n\n不利対面のキャラ\n・ほぼ全キャラ※自衛カードに当たってくれたら勝てるかもしれない\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/230412#link05")

@bot.command()
async def ソル(ctx):
	await ctx.send("ソルの情報\n\n組んで相性の良いキャラ\n・周囲カノーネor周囲スタン持ち\n・転倒させることができるカードを積んでいるキャラ\n\n有利対面のキャラ\n・体力倍率が0.90以下のキャラ全て\n\n不利対面のキャラ\n・フルカノ持ちアタッカー\n・ノホ、デルミン\n・ルチ、ギルガメッシュ、イスタカ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/229147#link02")

@bot.command()
async def ディズィー(ctx):
	await ctx.send("ディズィーの情報\n\n組んで相性の良いキャラ\n・HSで相手を確実に倒せるキャラ全て\n・トマス、ノホなどHSを相手に吐かせることができるキャラ\n\n有利対面のキャラ\n・ルチアーノ\n・自分より足が遅いキャラクター\n\n不利対面のキャラ\n・マルコス\n・デルミン\n・自分より射程が長いガンナー\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/230728#link05")

@bot.command()
async def グスタフ(ctx):
	await ctx.send("†世界最強のサポ兼アタッカーキャラグスタフの情報†\n\n組んで相性の良いキャラ\n・全てのキャラクター\n↑自分でも書いててバカらしくなってくるね\n\n有利対面のキャラ\n・周囲スタン、周囲カノーネを当てられたらとれる\n\n不利対面のキャラ\n・お母さん持ち\n・アバカン持ち\n・イデア持ち(ポータル回復カードがあれば不利にはならない)\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/251781#link05")

@bot.command()
async def テスラ(ctx):
	await ctx.send("テスラの情報\n\n組んで相性の良いキャラ\n・ルルカ\n・デルミン\n・カノーネ持ちのアタッカー\n\n耐え難いキャラ\n・ルチ、ギルガメッシュ、イスタカ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/251256#link08")

@bot.command()
async def ミク(ctx):
	await ctx.send("ミクの情報\n\n組んで相性の良いキャラ\n・フルカノ持ちアタッカー\n・デルミン\n・グスタフ\n\n耐え難いキャラ\n・ガンナー全般\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/261015#link02")

@bot.command()
async def ヴィオレッタ(ctx):
	await ctx.send("ヴィオレッタの情報\n\n組んで相性の良いキャラ\n・ポロロッチョ\n・デルミン\n\n耐え難いキャラ\n・お母さん持ちガンナー\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/282804#link05")

@bot.command()
async def ソーン(ctx):
	await ctx.send("ソーンの情報\n\n組んで相性の良いキャラ\n・アダム\n・忠臣\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・自分より射程が短いキャラ\n\n不利対面のキャラ\n・マルコス、デルミン\n・リリカ、まとい\n・マジスク＆ゆらら持ち\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/391208#link05")







bot.run(token)
