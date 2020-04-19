import discord
from discord.ext import commands
import random
import os
import traceback
import requests
from bs4 import BeautifulSoup
import time
import asyncio

bot = commands.Bot(command_prefix='！')
token = os.environ['DISCORD_BOT_TOKEN']
pong = random.randrange(10)
bot.remove_command('help')

god = [263614623238848522]
sub_god = [263614623238848522,347747169387937793]
def check_god(ctx):
	return ctx.message.author.id in god
def check_god2(ctx):
	return ctx.message.author.id in sub_god

rireki_text = {}
rireki = {}

atk = ["ノホ","忠臣","マルコス","ソル","リュウ","アダム","マリア","レム","カイ","ポロロッチョ","リヴァイ","デルミン","セイバー","ルルカ"]
gun = ["リリカ","ルチアーノ","まとい","ディズィー","サーティーン","エミリア","めぐめぐ","リン","イスタカ","ソーン","オカリン","猫宮","ギルガメッシュ"]
tank = ["ジャスティス","ジャンヌ","ヴィオレッタ","グスタフ","レン","モノクマ","めぐみん","トマス"]
supri = ["アタリ","ボイドール","テスラ","ミク","コクリコ","春麗","ザクレイ","勇者","きらら","アクア","レイヤ","ピエール"]
lol = {"1":"アタッカー","2":"ガンナー","3":"タンク","4":"スプリンター"}
llevel = {"1":"4~119","2":"120~159","3":"160~199","4":"200~240"}
mmedal = {"1":"アイコンなし","2":"銅アイコン経験あり","3":"銀アイコン経験あり","4":"金アイコンor公式大会優勝経験あり"}
yyn = {"1":"可能","2":"聞き専なら可能","3":"聞き専も不可能","4":"応相談"}
ynn = {"1":"オン","2":"オフ"}

all_roll = atk+gun+tank+supri
lll = [atk,gun,tank,supri]


atk_plo = {}
gun_plo = {}
tank_plo = {}
supri_plo = {}

osirase = ['None']

compass = {
	"アタリ":"アタリの情報※HS発動時のみ記載\n\n組んで相性の良いキャラ\n・マルコス＆リリカ\n・ディズィー\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・全てのキャラに有利\n\n不利対面\n①貫通\n②毒、サイレント、スタンなどの状態異常\n③ダメカ破壊\n④防御UP中に防御ダウン\n⑤カードキャンセル\n上記のものどれか一つでもまともに食らえば不利になる。\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/229151#link05",
	"ジャスティス":"ジャスティスの情報\n\n組んで相性の良いキャラ\n・ポロロッチョ\n・スタン持ち\n\n有利、不利対面のキャラ\n・相手にスタンと貫通がなければ有利、あれば不利\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/232405#link05",
	"リリカ":"リリカの情報\n\n組んで相性の良いキャラ\n・マルコス\n・アタリ\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・自分より射程の短いガンナー\n・ソーン\n\n不利対面のキャラ\n・足の速いアタッカー\n・ギルガメッシュ\n・攻撃寄りスプリンター\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/230284#link05",
	"ノホ":"ノホの情報\n\n組んで相性の良いキャラ\n・ディズィー\n・トマス\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・体力倍率が0.85以下のキャラほぼ全て(マジスク＆ゆらら前提)\n\n不利対面のキャラ\n・ギルガメッシュ\n・グスタフ\n・きらら\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/232243#link05",
	"忠臣":"忠臣の情報\n\n組んで相性の良いキャラ\n・射程の長いガンナー\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・体力倍率0.8以下のキャラ\n\n不利対面のキャラ\n・自分より足が速いキャラ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/231602#link05",
	"ジャンヌ":"ジャンヌの情報\n\n組んで相性の良いキャラ\n・ポロロッチョ\n・デルミン\n\n耐えやすい対面\n・サーティーン\n・ノホ\n・リリカ\n\n耐え難い対面\n・オカリン\n・ルチアーノ\n・忠臣\n・イスタカ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/229854#link05",
	"ボイドール":"ボイドールの情報\n\n組んで相性の良いキャラ\n・トマス\n・ボイドの型によって幅広いアタッカー、ガンナーと組みやすい\n\n耐え難い対面\n・お母さん入りガンナー\n・マジスク&貫通持ち\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/231086#link05",
	"マルコス":"マルコスの情報\n\n組んで相性の良いキャラ\n・リリカ\n・アタリ\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・枝でのカードキャンセルが成功すればほぼ全キャラ\n\n不利対面のキャラ(HSゲージが溜まっていれば対処可)\n・周囲カノーネ持ち\n・マジスク＆ゆらら持ち\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/229810#link05",
	"ルチアーノ":"ルチアーノの情報\n\n組んで相性の良いキャラ\n・カノーネ持ちキャラクター全般\n・周囲の発動がが速いキャラクター\n\n有利対面のキャラ\n・ディーバのみアタッカー全般\n\n不利対面のキャラ\n・マルコス\n・デルミン\n・自分より射程が長いガンナー\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/232197#link05",
	"まとい":"まといの情報\n\n組んで相性の良いキャラ\n・ヴィオレッタ\n・フルカノアタッカー\n\n有利対面のキャラ\n・ディズィー\n・ソーン\n\n不利対面のキャラ\n・ほぼ全キャラ※自衛カードに当たってくれたら勝てるかもしれない\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/230412#link05",
	"ソル":"ソルの情報\n\n組んで相性の良いキャラ\n・周囲カノーネor周囲スタン持ち\n・転倒させることができるカードを積んでいるキャラ\n\n有利対面のキャラ\n・体力倍率が0.90以下のキャラ全て\n\n不利対面のキャラ\n・フルカノ持ちアタッカー\n・ノホ、デルミン\n・ルチ、ギルガメッシュ、イスタカ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/229147#link02",
	"ディズィー":"ディズィーの情報\n\n組んで相性の良いキャラ\n・HSで相手を確実に倒せるキャラ全て\n・トマス、ノホなどHSを相手に吐かせることができるキャラ\n\n有利対面のキャラ\n・ルチアーノ\n・自分より足が遅いキャラクター\n\n不利対面のキャラ\n・マルコス\n・デルミン\n・自分より射程が長いガンナー\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/230728#link05",
	"グスタフ":"†世界最強のサポ兼アタッカーキャラグスタフの情報†\n\n組んで相性の良いキャラ\n・全てのキャラクター\n↑自分でも書いててバカらしくなってくるね\n\n有利対面のキャラ\n・周囲スタン、周囲カノーネを当てられたらとれる\n\n不利対面のキャラ\n・お母さん持ち\n・アバカン持ち\n・イデア持ち(ポータル回復カードがあれば不利にはならない)\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/251781#link05",
	"テスラ":"テスラの情報\n\n組んで相性の良いキャラ\n・ルルカ\n・デルミン\n・カノーネ持ちのアタッカー\n\n耐え難いキャラ\n・ルチ、ギルガメッシュ、イスタカ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/251256#link08",
	"ミク":"ミクの情報\n\n組んで相性の良いキャラ\n・フルカノ持ちアタッカー\n・デルミン\n・グスタフ\n\n耐え難いキャラ\n・ガンナー全般\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/261015#link02",
	"ヴィオレッタ":"ヴィオレッタの情報\n\n組んで相性の良いキャラ\n・ポロロッチョ\n・デルミン\n\n耐え難いキャラ\n・お母さん持ちガンナー\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/282804#link05",
	"ソーン":"ソーンの情報\n\n組んで相性の良いキャラ\n・アダム\n・忠臣\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・自分より射程が短いキャラ\n\n不利対面のキャラ\n・マルコス、デルミン\n・リリカ、まとい\n・マジスク＆ゆらら持ち\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/391208#link05",
	"コクリコ":"コクリコの情報\n\n組んで相性の良いキャラ\n・HS発動時はアタッカー、ガンナー全キャラに合う\n・フルカノアタッカー\n・ディズィー\n\n有利対面のキャラ\n・初手のみマルコス＆リリカ\n・ダメカを積んでたらカノーネがないキャラ\n・防御バフカードを積んでいたらお母さんがないキャラ\n\n不利対面\n・ソル\n・ギルガメッシュ\n・貫通カードを持っているキャラ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/281658#link02",
	"リュウ":"リュウの情報\n\n組んで相性の良いキャラ\n・周囲カノーネor周囲スタン持ち\n・ディズィー\n・ギルガメッシュ\n・春麗\n\n有利対面のキャラ※HSが溜まってる場合のみ\n・ダメカがないキャラ全部\n・遠距離or周囲持ちヒーロー\n\n不利対面\n・マルコス＆リリカ\n・デルミン\n・ノホ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/296611#link02",
	"アダム":"アダムの情報\n\n組んで相性の良いキャラ\n・デズ\n・ギルガメッシュ\n・ルチアーノ\n・めぐみん\n\n有利対面のキャラ\n・ギルガメッシュ以外のガンナー全般\n・体力倍率0.75以下のキャラほぼ全て\n\n・2凸以上のマルコス\n・デルミン\n・イスタカ\n・マリア\n・ギルガメッシュ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/313514#link05",
	"イスタカ":"イスタカの情報\n\n組んで相性の良いキャラ\n・ダメカ破壊があるキャラ\n\n有利対面のキャラ\n・基本全有利\n\n不利対面\n・きらら\n・デルミン\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/365276#link05",
	"リン":"リンの情報\n\n組んで相性の良いキャラ\n・セイバー\n・アダム\nデルミン\n・ノホ\n・マリア\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・イスタカ以外のガンナー全般\n・マルコス&リリカ(諸説)\n\n不利対面のキャラ\n・デルミン\n・アダム\n・イスタカ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/355191#link02",
	"デルミン":"デルミンの情報\n\n組んで相性の良いキャラ\n・トマス\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・基本ガンナー全般\n・アダム、ソル\n\n不利対面\n・周囲カノーネ持ち\n・マリア\n・格上ガンナーからのUR貫通遠距離\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/400270#link05",
	"リヴァイ":"リヴァイの情報\n\n組んで相性の良いキャラ\n・近距離、周囲の発動が速いスプリンターとタンク全て\n\n有利対面のキャラ\n・エミリア\n・ディズィー\n・ポロロッチョ\n・マリア\n\n不利対面のキャラ\n・ノホ\n・イスタカ\n・近距離、周囲スタンor周囲ダメカ破壊、ゆらら持ち全キャラ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/397046#link06",
	"猫宮":"猫宮の情報\n\n組んで相性の良いキャラ\n・ダメカ破壊持ち※周囲がおすすめ\n・スタンorサイレントの状態異常カード持ち\n\n有利対面のキャラ\n・自分より射程が同じかそれ以下のガンナーほぼ全て(アサルト時のみ)\n・遠距離持ちのアタッカーほぼ全て\n\n不利対面のキャラ\n・自分より射程の長いガンナー全て\n・マジスク＆ゆらら持ちキャラ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/414356#link05",
	"アクア":"アクアの情報\n\n組んで相性の良いキャラ\n・マリア\n・マジスクを持ってるアタッカー\n・オカリン\n・ギル\n\n有利対面のキャラ\n・ディズィー\n・ソーン\n\n不利対面のキャラ\n・レイヤ\n・きらら\n・ルチアーノ\n・勇者\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/388828#link02",
	"ピエール":"ピエールの情報\n\n組んで相性の良いキャラ\n・支援系を除く全てのキャラ\n\n耐え難い対面\n・ギルガメッシュ\n・オカリン\n・ルチアーノ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/452335#link05",
 	"セイバー":"セイバーの情報\n\n組んで相性の良いキャラ\n・ディズィー\n・デッキ次第で攻撃系キャラならなんでも合う\n・グスタフ\n\n有利体面のキャラ\n・ギル、イスタカ以外のガンナー全般\n・きらら\n\n不利対面のキャラ\n・アダム\n・デルミン\n・ギル、イスタカ\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/436927#link05",
 	"マリア":"まだ書かれていません！ごめんなさい",
 	"サーティーン":"まだ書かれていません！ごめんなさい",
 	"勇者":"まだ書かれていません！ごめんなさい",
 	"エミリア":"まだ書かれていません！ごめんなさい",
 	"レム":"まだ書かれていません！ごめんなさい",
 	"カイ":"まだ書かれていません！ごめんなさい",
 	"メグメグ":"まだ書かれていません！ごめんなさい",
 	"レン":"まだ書かれていません！ごめんなさい",
 	"トマス":"まだ書かれていません！ごめんなさい",
 	"モノクマ":"まだ書かれていません！ごめんなさい",
 	"オカリン":"まだ書かれていません！ごめんなさい",
 	"ギルガメッシュ":"まだ書かれていません！ごめんなさい",
 	"ルルカ":"まだ書かれていません！ごめんなさい",
 	"レイヤ":"零夜の情報\n\n組んで相性の良いキャラ\n・トマス\n・リン\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・ダメージカットが1枚以下のキャラ\n・マリア\n・オカリン\n\n不利対面のキャラ\n・ギルガメッシュ\n・イスタカ\n・ダメージカットの枚数が負けていたら猫宮\n\n相性の良いカード、立ち回り等\nhttps://games.app-liv.jp/archives/429859#link05",
 	"めぐみん":"まだ書かれていません！ごめんなさい",
 	"ザクレイ":"まだ書かれていません！ごめんなさい",
	"きらら":"まだ書かれていません！ごめんなさい",
	"春麗":"まだ書かれていません！ごめんなさい"
}




@bot.command()
async def ランダムパーティー(ctx):
	pt = []
	await ctx.send("勝手にパーティーを決めます")
	romm = random.sample(lll,k=3)
	for r in romm:
		for ii in random.choice(r):
			pt.append(ii)
	await ctx.send("".join(pt))

@bot.command()
async def ランダム(ctx):
	await ctx.send(random.choice(all_roll))

@bot.command()
async def ランダムアタッカー(ctx):
	await ctx.send(random.choice(atk))

@bot.command()
async def ランダムガンナー(ctx):
	await ctx.send(random.choice(gun))

@bot.command()
async def ランダムタンク(ctx):
	await ctx.send(random.choice(tank))

@bot.command()
async def ランダムスプリンター(ctx):
	await ctx.send(random.choice(supri))


@bot.command()
async def ヘルプ(ctx):
	embed = discord.Embed(title="このbotの説明書",description="コマンド見にくくてごめん。")
	embed.add_field(name="！コンパスの後に表示されているキャラ名を入力",value="コンパスのキャラについて解説するよ。\nキャラは相性の良いキャラと有利対面、不利対面を出します。\n対面については全てタイマンを想定しています。\n有利、不利は全キャラ書いてないので経験で頑張ってみてね\n耐久型キャラクターのタイマンは倒されやすいかどうかを書いています。\n\nおすすめカードと立ち回りについては\nhttps://twitter.com/compass_AG\nの記事を引用しています。",inline=False)
	embed.add_field(name="！ランダム",value="何のキャラで遊ぶか中々決まらない時にランダムで決めちゃうよ\nランダムの後にロール名を入力すると更に絞れるよ",inline=False)
	embed.add_field(name="！バイオハザード",value="https://japan-cov-19.now.sh/\nから最新のコロナ感染者の情報を５件表示するよ",inline=False)
	embed.add_field(name="！招待URL",value="このbotを他のサーバーに入れるためのURLが出てくるよ",inline=False)
	embed.add_field(name="！登録",value="自分のプロフィールを登録するよ。\n既に登録していても何度でも再登録できるよ。",inline=False)
	embed.add_field(name="！プロフィール",value="自分のプロフィールを表示するよ。",inline=False)
	embed.add_field(name="！サーチ",value="例「！サーチプロフィール」・プロフィール\nこのコマンドの後にグループメンバーのメンションするとメンションした人のプロフィールを出すよ\n・ロール名\nプロフィール検索をオンにした登録してある人のプロフィールをランダムに出すよ",inline=False)
	embed.add_field(name="！最新ブログ",value="ariria.com\nから最新の記事を持ってくるよ。",inline=False)
	embed.add_field(name="！お知らせ",value="botについてのお知らせを表示するよ",inline=False)
	embed.add_field(name="作者",value="コンパスで語ってることが間違っていたり、追加して欲しい機能があったら\nhttps://peing.net/ja/blalcxw2aqk2dbh?event=0\n↑に入れてね\nhttps://discord.gg/CE94F4t\n作業通話常に募集してるよ；；良ければ来てね",inline=False)
	await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
	pass

@bot.command()
async def ping(ctx):
	await ctx.send(pong)

@bot.command()
async def お知らせ(ctx):
	await ctx.send(osirase[0])
	
@bot.command()
async def サーチアタッカー(ctx):
	sati = random.choice([i for i in atk_plo.values()])
	await ctx.send(sati)

@bot.command()
async def サーチガンナー(ctx):
	sati = random.choice([i for i in gun_plo.values()])
	await ctx.send(sati)

@bot.command()
async def サーチタンク(ctx):
	sati = random.choice([i for i in tank_plo.values()])
	await ctx.send(sati)

@bot.command()
async def サーチスプリンター(ctx):
	sati = random.choice([i for i in supri_plo.values()])
	await ctx.send(sati)

@bot.command()
async def 最新ブログ(ctx):
	url = "http://ariria.com/"
	res = requests.get(url).text
	soup = BeautifulSoup(res, 'html.parser')
	ariria = soup.find_all('h2',class_= "entry-title",itemprop="headline")
	ari = ariria[1].find("a")
	await ctx.send(ariria[1].get_text()+'\n'+ari.get("href"))

#コマンドエラーが起きてしまうから無理矢理passで対応しちゃってる
@bot.event
async def on_message(message):
	if message.author.id != 685676747173134337:
		if message.content == "！登録":
			m_id = message.author.id
			channel = message.channel
			await channel.send("登録を開始します。まずは主に使用するキャラ1人教えてください")
			def check_mes(message):
				return message.author.id == m_id and message.channel == channel
			def check_roll(message):
				return message.content in all_roll and message.channel == channel and message.author.id == m_id
			def check_level(message):
				return message.content in llevel and message.channel == channel and message.author.id == m_id
			def check_medal(message):
				return message.content in mmedal and message.channel == channel and message.author.id == m_id
			def check_yn(message):
				return message.content in yyn and message.channel == channel and message.author.id == m_id
			def check_n(message):
				return message.content in ynn and message.channel == channel and message.author.id == m_id
			try:
				roll = await bot.wait_for('message', timeout=30.0, check=check_roll)
			except asyncio.TimeoutError:
				await channel.send("タイムアウトしたよ。最初からやり直してね")
			else:
				roll = roll.content
				await channel.send('デッキの合計レベルを番号で教えてください\n1:4~119 2:120~159 3:160~199 4:200~240'.format(roll))
				try:
					level = await bot.wait_for('message', timeout=30.0, check=check_level)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					level = llevel[level.content]
					await channel.send("実力を番号で教えてください\n1:参加賞 2:銅アイコン経験あり 3:銀アイコン経験あり 4:金アイコンor公式大会優勝経験あり".format(level))
					try:
						medal = await bot.wait_for('message', timeout=30.0, check=check_medal)
					except asyncio.TimeoutError:
						await channel.send("タイムアウトしたよ。最初からやり直してね")
					else:
						medal = mmedal[medal.content]
						await channel.send("通話が可能かどうか番号で教えてください\n1:可能 2:聞き専なら可能 3:聞き専も不可 4:応相談".format(medal))
						try:
							yn = await bot.wait_for('message', timeout=30.0, check=check_yn)
						except asyncio.TimeoutError:
							await channel.send("タイムアウトしたよ。最初からやり直してね")
						else:
							yn = yyn[yn.content]
							await channel.send("何か一言をお願いします".format(yn))
							try:
								hitokoto = await bot.wait_for('message', timeout=30.0, check=check_mes)
							except asyncio.TimeoutError:
								await channel.send("タイムアウトしたよ。最初からやり直してね")
							else:
								await channel.send("ツイッターのIDをURLで載せてください\nない場合は適当な文字を入力してください".format(hitokoto))
								try:
									twit = await bot.wait_for('message', timeout=30.0, check=check_mes)
								except asyncio.TimeoutError:
									await channel.send("タイムアウトしたよ。最初からやり直してね")
								else:
									if "https://twitter.com/" in twit.content:
										await channel.send("プロフィールの検索を許可しますか？\n1:許可する 2:許可しない".format(check_mes))
										try:
											saticheck = await bot.wait_for('message', timeout=30.0, check=check_n)
										except asyncio.TimeoutError:
											await channel.send("タイムアウトしたよ。最初からやり直してね")
										else:
											if saticheck.content == "1":
												if m_id in sub_god:rireki_text[m_id] = '名前:'+message.author.name+"#"+message.author.discriminator+"\nbotの権限:あり\n使用キャラ:"+roll+"\nデッキレベル:"+level+"\n実力:"+medal+"\n通話について:"+yn+"\n一言:"+hitokoto.content+"\nツイッター:"+twit.content
												else:rireki_text[m_id] = '名前:'+message.author.name+"#"+message.author.discriminator+"\nbotの権限:なし\n使用キャラ:"+roll+"\nデッキレベル:"+level+"\n実力:"+medal+"\n通話について:"+yn+"\n一言:"+hitokoto.content+"\nツイッター:"+twit.content
												if roll in atk:atk_plo[message.author.id] = rireki_text[message.author.id]
												if roll in gun:gun_plo[message.author.id] = rireki_text[message.author.id]
												if roll in tank:tank_plo[message.author.id] = rireki_text[message.author.id]
												if roll in supri:supri_plo[message.author.id] = rireki_text[message.author.id]
												await channel.send(rireki_text[m_id]+"\n\nこの内容で登録しました。".format(saticheck))
											if saticheck.content == "2":
												if m_id in sub_god:rireki_text[m_id] = '名前:'+message.author.name+"\n\nbotの権限:あり\n使用キャラ:"+roll+"\nデッキレベル:"+level+"\n実力:"+medal+"\n通話について:"+yn+"\n一言:"+hitokoto.content
												else:rireki_text[m_id] = '名前:'+message.author.name+"\n\nbotの権限:なし\n使用キャラ:"+roll+"\nデッキレベル:"+level+"\n実力:"+medal+"\n通話について:"+yn+"\n一言:"+hitokoto.content
												await channel.send(rireki_text[m_id]+"\n\nこの内容で登録しました。".format(saticheck))
									if "https://twitter.com/" not in twit.content:
										await channel.send("プロフィールの検索を許可しますか？\n1:許可する 2:許可しない".format(check_mes))
										try:
											saticheck = await bot.wait_for('message', timeout=30.0, check=check_n)
										except asyncio.TimeoutError:
											await channel.send("タイムアウトしたよ。最初からやり直してね")
										else:
											if saticheck.content == "1":
												if m_id in sub_god:rireki_text[m_id] = '名前:'+message.author.name+"#"+message.author.discriminator+"\nbotの権限:あり\n使用キャラ:"+roll+"\nデッキレベル:"+level+"\n実力:"+medal+"\n通話について:"+yn+"\n一言:"+hitokoto.content
												else:rireki_text[m_id] = '名前:'+message.author.name+"#"+message.author.discriminator+"\nbotの権限:なし\n使用キャラ:"+roll+"\nデッキレベル:"+level+"\n実力:"+medal+"\n通話について:"+yn+"\n一言:"+hitokoto.content
												if roll in atk:atk_plo[message.author.id] = rireki_text[message.author.id]
												if roll in gun:gun_plo[message.author.id] = rireki_text[message.author.id]
												if roll in tank:tank_plo[message.author.id] = rireki_text[message.author.id]
												if roll in supri:supri_plo[message.author.id] = rireki_text[message.author.id]
												await channel.send(rireki_text[m_id]+"\n\nこの内容で登録しました。".format(saticheck))
											if saticheck.content == "2":
												if m_id in sub_god:rireki_text[m_id] = '名前:'+message.author.name+"\nbotの権限:あり\n使用キャラ:"+roll+"\nデッキレベル:"+level+"\n実力:"+medal+"\n通話について:"+yn+"\n一言:"+hitokoto.content
												else:rireki_text[m_id] = '名前:'+message.author.name+"#"+message.author.discriminator+"\nbotの権限:なし\n使用キャラ:"+roll+"\nデッキレベル:"+level+"\n実力:"+medal+"\n通話について:"+yn+"\n一言:"+hitokoto.content
												await channel.send(rireki_text[m_id]+"\n\nこの内容で登録しました。".format(saticheck))
		if message.content == "！プロフィール":
			channel = message.channel
			m_id = message.author.id
			if m_id in rireki_text.keys():
				await channel.send(f'{message.author.mention}さんのプロフィール\n'+rireki_text[m_id])
			else:await channel.send(f"{message.author.mention}さんはまだ登録されていません。「！登録」でプロフィールを入力してください")
		if message.content == "！コンパス":
			channel = message.channel
			embed = discord.Embed(title="何が知りたいの？",description="キャラ名を書き込んでね")
			embed.add_field(name="アタッカー",value=atk,inline=False)
			embed.add_field(name="\nガンナー",value=gun,inline=False)
			embed.add_field(name="\nスプリンター",value=supri,inline=False)
			embed.add_field(name="\nタンク",value=tank,inline=False)
			await channel.send(embed=embed)	
			def check(message):
				return message.content in [i for i in compass.keys()] and message.channel == channel
			try:
				msg = await bot.wait_for('message', timeout=30.0, check=check)
			except asyncio.TimeoutError:
				await message.delete()
				await channel.send("タイムアウトしたよ。最初からやり直してね")
			else:
				await channel.send(compass[msg.content].format(msg))
		if message.author.id in god:
			if message.content == "辞書編集":
				channel = message.channel
				await channel.send("どうぞ")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=30.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					await channel.send(com.content+"の内容をどうぞ")
					try:
						comm = await bot.wait_for('message', timeout=30.0, check=check_mes)
					except asyncio.TimeoutError:
						await channel.send("タイムアウトしたよ。最初からやり直してね")
					else:
						compass[com.content] = comm.content
						await channel.send(com.content+"\n"+comm.content)
			if message.content == "アタッカー追加":
				channel = message.channel
				await channel.send("どうぞ")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=30.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					atk.append(com.content)
					await channel.send(com.content+"をアタッカーに追加しました")
			if message.content == "ガンナー追加":
				channel = message.channel
				await channel.send("どうぞ")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=30.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					gun.append(com.content)
					await channel.send(com.content+"をガンナーに追加しました")
			if message.content == "タンク追加":
				channel = message.channel
				await channel.send("どうぞ")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=30.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					tank.append(com.content)
					await channel.send(com.content+"をタンクに追加しました")
			if message.content == "スプリンター追加":
				channel = message.channel
				await channel.send("どうぞ")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=30.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					supri.append(com.content)
					await channel.send(com.content+"をスプリンターに追加しました")
			if message.content == "アタッカー削除":
				channel = message.channel
				await channel.send("どうぞ")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=30.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					atk.remove(com.content)
					await channel.send(com.content+"をアタッカーから削除しました")
			if message.content == "ガンナー削除":
				channel = message.channel
				await channel.send("どうぞ")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=30.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					gun.remove(com.content)
					await channel.send(com.content+"をガンナーから削除しました")
			if message.content == "タンク削除":
				channel = message.channel
				await channel.send("どうぞ")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=30.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					tank.remove(com.content)
					await channel.send(com.content+"をタンクから削除しました")
			if message.content == "スプリンター削除":
				channel = message.channel
				await channel.send("どうぞ")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=30.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					supri.remove(com.content)
					await channel.send(com.content+"をスプリンターから削除しました")
			if message.content == "お知らせ":
				channel = message.channel
				await channel.send("お知らせすることを書き込んでください")
				def check_mes(message):
					return message.author.id in god and message.channel == channel
				try:
					com = await bot.wait_for('message', timeout=300.0, check=check_mes)
				except asyncio.TimeoutError:
					await channel.send("タイムアウトしたよ。最初からやり直してね")
				else:
					osirase[0] = com.content
					await channel.send(com.content+"をお知らせ欄に追加しました")
	await bot.process_commands(message)
@bot.command()
async def バイオハザード(ctx):
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
	
@bot.command(pass_context=True, name="kick")
@commands.check(check_god2)
async def kick(ctx, member: discord.Member, *, reason=None):
	if member.id in sub_god:ctx.send(f"{member.mention}も権限を持ってるみたいだね")
	else:
		try:
			await member.kick(reason=reason)
			await ctx.send(f"{member.mention}をキックしちゃったぜ！笑")
		except:await ctx.send("すみません。なんでもないです。")
@bot.command()
@commands.check(check_god2)
async def 追加(ctx, member: discord.Member, *, reason=None):
	sub_god.append(member.id)
	await ctx.send(f"{member.mention}様にbot専用の権限を付与しました")

@bot.command()
@commands.check(check_god)
async def 一括削除(ctx):
	sub_god = [263614623238848522,347747169387937793,598640625142726668,483573525974614017,276000856556437504]
	await ctx.send("特別な人以外の権限を全て剥奪しました")

@bot.command()
@commands.check(check_god)
async def 削除(ctx, member: discord.Member, *, reason=None):
	sub_god.remove(member.id)
	await ctx.send(f"{member.mention}様からbot専用の権限を削除しました")
	

@bot.command()
async def サーチプロフィール(ctx, member: discord.Member, *, reason=None):
	if member.id in rireki_text.keys():
		await ctx.send(f'{member.mention}さんのプロフィールを表示します\n'+rireki_text[member.id])
	else:await ctx.send(f"{member.mention}さんはまだ登録されていません。")


@bot.command()
@commands.check(check_god)
async def グループ表示(ctx):
	for guild in bot.guilds:
		await ctx.send(guild)

@bot.command()
@commands.check(check_god)
async def チェック(ctx):
	await ctx.send("今、権限を持っている人は"+str(len(sub_god))+"人いるよ")

@bot.command()
async def 権限確認(ctx, member: discord.Member, *, reason=None):
	if member.id in sub_god:
		await ctx.send("この人はbotの権限を持っているよ")
	else:await ctx.send("この人はbotの権限を持っていないよ笑")
bot.run(token)
