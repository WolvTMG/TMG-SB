import discord
from discord.ext import commands
from colorama import Fore
from pyfiglet import Figlet
from http.client import HTTPException
from datetime import datetime
from pytz import timezone
from utils.common import *

from utils.settings import *


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def activity(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ini\n[streaming] streaming activity\n[playing] playing activity\n[listening] listen activity\n[watching] watches activity\n[stopactivity] stops activity\n\n[{watermark}]```", delete_after=8)
        
    @commands.command()
    async def streaming(self, ctx, *, message):
        await ctx.message.delete()
        stream = discord.Streaming(
            name=message,
            url="https://www.twitch.tv/tmgwolv", # u can change this to what ever as long as it's a working twitch url
        )
        await self.bot.change_presence(activity=stream)

    @commands.command()
    async def playing(self, ctx, *, message):
        await ctx.message.delete()
        game = discord.Game(
            name=message
        )
        await self.bot.change_presence(activity=game)

    @commands.command()
    async def listening(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=message,
            ))

    @commands.command()
    async def watching(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=message
            ))

    @commands.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
    async def stopactivity(self, ctx):
        await ctx.message.delete()
        await self.bot.change_presence(activity=None, status=discord.Status.dnd)

    @commands.command()
    async def customstatus(self, ctx, text):
        await ctx.message.delete()

        text = []
        text.append(ctx.content)

        # for i in text:
        #     self.discord.Activity(activity=discord.Activity(name=i, type=5))

        print(text)


def setup(bot):
    bot.add_cog(Commands(bot))
