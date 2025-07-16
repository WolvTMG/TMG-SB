import requests
from discord.ext import commands
from colorama import Fore
from pyfiglet import Figlet
import requests
from http.client import HTTPException
from datetime import datetime
from pytz import timezone

from utils.settings import *
 

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def crypto(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ini\n[btc] bitcoin\n[eth] etherum\n[xmr] xmr\n[xrp] xrp\n[doge] dogecoin\n\n[{watermark}]```", delete_after=8)
 
    @commands.command()
    async def btc(self, ctx):
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def xmr(self, ctx):
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def xrp(self, ctx):
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def doge(self, ctx):
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def eth(self, ctx):
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def raven(self, ctx):
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=RVN&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

def setup(bot):
    bot.add_cog(Commands(bot))
