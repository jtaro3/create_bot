import os
import random
from datetime import datetime

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN が設定されていません。.env.example を参考に .env を作成してください。"
    )

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} でログインしました")


@bot.command(aliases=["h"])
async def hello(ctx):
    await ctx.send("こんにちは！Botは正常に動いています 🤖")


@bot.command(aliases=["p"])
async def ping(ctx):
    await ctx.send("Pong! 🏓")


@bot.command(aliases=["t"])
async def time(ctx):
    now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    await ctx.send(f"現在時刻は {now} です 🕐")


@bot.command(aliases=["d"])
async def dice(ctx):
    number = random.randint(1, 6)
    await ctx.send(f"🎲 サイコロの結果は **{number}** です！")


@bot.command(name="helpme", aliases=["ヘ"])
async def helpme(ctx):
    message = """
🤖 **Botコマンド一覧**

`!h` / `!hello` → Botに挨拶
`!p` / `!ping`  → Botの応答確認
`!t` / `!time`  → 現在時刻
`!d` / `!dice`  → サイコロを振る
`!ヘ` / `!helpme` → この一覧を表示
"""
    await ctx.send(message)


bot.run(TOKEN)
