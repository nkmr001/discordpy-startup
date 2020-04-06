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
async def ヘルプ(ctx)
    await ctx.send("/キャラ名でそのキャラの相性の良いキャラと有利対面、不利対面を出します。\n対面については全てタイマンを想定しています
                   
@bot.command()
async def アタリ(ctx)
    await ctx.send("アタリの情報※HS発動時のみ記載\n組んで相性の良いキャラ\n・マルコス＆リリカ\n・ディズィー\n・周囲カノーネor周囲スタン持ち\n\n有利対面のキャラ\n・全てのキャラに有利\n不利対面\n①貫通\n②毒、サイレント、スタンなどの状態異常\n③ダメカ破壊\n④防御UP中に防御ダウン\n⑤カードキャンセル\n上記のものどれか一つでもまともに食らえば不利になる。")　　　　　　　　　　　　　　　　
        
@bot.command()
async def ジャスティス(ctx)                  
                   
@bot.command()
async def リリカ(ctx)

@bot.command()
async def ノホ(ctx)
                   
@bot.command()
async def 忠臣(ctx)                   
                   
@bot.command()
async def ジャンヌ(ctx)                   
                   
                   
@bot.command()
async def マルコス(ctx)
                   
@bot.command()
async def ルチアーノ(ctx)                   
                   
@bot.command()
async def ボイドール(ctx)                   
                   
                   
@bot.command()
async def まとい(ctx)                   
                   
@bot.command()
async def ソル(ctx)                   
                   
                   
@bot.command()
async def ディズィー(ctx)                   
                   
                   
@bot.command()
async def グスタフ(ctx)
                   
                  
@bot.command()
async def テスラ(ctx)
                   
                   
@bot.command()
async def ミク(ctx)
                   
                   
@bot.command()
async def ヴィオレッタ(ctx)                  
                   
                   
@bot.command()
async def コクリコ(ctx)                   
                   
@bot.command()
async def リュウ(ctx)                   
                   
@bot.command()
async def 春麗(ctx)                   
                   
@bot.command()
async def マリア(ctx)
                   
@bot.command()
async def アダム(ctx)                  
                   
@bot.command()
async def サーティーン(ctx)                   
                   
                   
@bot.command()
async def 勇者(ctx)                   
                   
@bot.command()
async def エミリア(ctx)                   
                   
                   
@bot.command()
async def レム(ctx)                   
                   
                   
 @bot.command()
async def カイ(ctx)                  
                   
                   
@bot.command()
async def メグメグ(ctx)                  
                   
@bot.command()
async def リン(ctx)                   
                   
@bot.command()
async def レン(ctx)                   
                   
@bot.command()
async def イスタカ(ctx)                   
                   
@bot.command()
async def ザクレイ(ctx)                   
                   
@bot.command()
async def きらら(ctx)                   
                   
@bot.command()
async def モノクマ(ctx)                   
                   
@bot.command()
async def ポロロッチョ(ctx)
                   
@bot.command()
async def アクア(ctx)                  
                   
@bot.command()
async def めぐみん(ctx)                  
                   
@bot.command()
async def ソーン(ctx)                   
                   
@bot.command()
async def リヴァイ(ctx)                   
                   
@bot.command()
async def デルミン(ctx)
                   
@bot.command()
async def トマス(ctx)                   
                   
@bot.command()
async def 猫宮(ctx)                   
                   
@bot.command()
async def オカリン(ctx)      
                   
@bot.command()
async def レイヤ(ctx)                   
                   
                   
@bot.command()
async def オルタ(ctx)
                   
                   
@bot.command()
async def ギルガメッシュ(ctx)                   
                   
                   
@bot.command()
async def ルルカ(ctx)                   
                   
@bot.command()
async def ピエール(ctx)                   
                   
                   
                   
bot.run(token)
