import discord
import discord.ext.commands
from discord.ext import commands
from colorama import Fore
from pyfiglet import Figlet
import requests
from http.client import HTTPException
import base64
import hashlib
from datetime import datetime
from pytz import timezone
from utils.common import *

from utils.settings import *


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def encryption(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ini\n[encode_base64] encrypt with base64\n[encode_md5] encrypt with md5\n[encode_sha1] encrypt with sha1\n[encode_sha384] encrpyt with sha384\n[encode_sha224] encrpy with sha224\n[encode_sha512] encrpy with sha512\n[encode_leet] encrpyt with leet\n\n[{watermark}]```", delete_after=8)

    @commands.command()
    async def encode_base64(self, ctx, *, args):
        await ctx.message.delete()
        msg = base64.b64encode('{}'.format(args).encode('ascii'))
        enc = str(msg)
        enc = enc[2:len(enc)-1]
        await ctx.send(enc)

    @commands.command()
    async def encode_md5(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.md5(args.encode())
        crnja = msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_sha1(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha1(args.encode())
        crnja = msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_sha384(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_384(args.encode())
        crnja = msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_sha224(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_224(args.encode())
        crnja = msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_sha512(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_512(args.encode())
        crnja = msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_leet(self, ctx, *, args):
        await ctx.message.delete()
        encoded = args.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o', '0').replace('O', '0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')
        await ctx.send(f'`{encoded}`')

def setup(bot):
    bot.add_cog(Commands(bot))
