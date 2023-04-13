import discord
from discord.ext import commands
from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def btc(ctx):
    btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
    await ctx.send(f"BTC 價格：{btc_price['price']}")

bot.run(DISCORD_BOT_TOKEN)
