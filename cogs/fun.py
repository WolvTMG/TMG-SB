import discord
import time
import requests
import io
import aiohttp
import warnings
from discord.ext import commands
import random
import sys
from colorama import Fore
from pyfiglet import Figlet
import os
import requests 
import base64
import hashlib
from pytz import timezone
import discord.ext.commands
from datetime import datetime
from http.client import HTTPException

from utils.common import *
from utils.settings import *


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fun(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ini\n[cf] coin flip\n[emoji] view emojis\n\n[{watermark}]```", delete_after=8)

    @commands.command()
    async def emoji(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ini\n[ak] emoji\n[awp] emoji\n[lmg] emoji\n\n[{watermark}]```", delete_after=8)

    @commands.command()
    async def cf(self, ctx):
        await ctx.message.delete()
        choose = ["Heads", "Tails"]
        cf = random.choice(choose)

        await ctx.send("```ini\n" + cf + f"\n\n[{watermark}]```", delete_after=8)

    @commands.command()
    async def ak(self, ctx):
        await ctx.message.delete()
        ak = '︻╦╤─'
        await ctx.send(ak, delete_after=8)

    @commands.command()
    async def awp(self, ctx):
        await ctx.message.delete()
        awp = '︻デ═一'
        await ctx.send(awp, delete_after=8)

    @commands.command()
    async def lmg(self, ctx):
        await ctx.message.delete()
        lmg = '︻╦̵̵͇╤──'
        await ctx.send(lmg, delete_after=8)

def setup(bot):
    bot.add_cog(Commands(bot))
