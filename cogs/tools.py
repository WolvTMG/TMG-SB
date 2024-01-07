import io
import os
import sys
import json
import time
import math
import random
import base64
import psutil
import GPUtil
import shutil
import aiohttp
import asyncio
import discord
import hashlib
import warnings
import requests
import platform
import subprocess
from colorama import Fore
from pytz import timezone
from pyfiglet import Figlet
import discord.ext.commands
from datetime import datetime
from discord.ext import commands
from colored import fg, attr, bg
from http.client import HTTPException
from weight_converter.convert import Kilograms, Pounds
from currency_converter import CurrencyConverter

from utils.common import *
from utils.settings import *

c = CurrencyConverter()


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        if isinstance(error, commands.CommandOnCooldown):
            message = f"{colorama.Fore.RESET}[{current_time}] {colorama.Fore.RED}[ERROR] {colorama.Fore.RESET} Cooldown: {round(error.retry_after, 1)} seconds"
        elif isinstance(error, commands.MissingPermissions):
            message = f"{colorama.Fore.RESET}[{current_time}] {colorama.Fore.RED}[ERROR] {colorama.Fore.RESET}Missing permissions"
        elif isinstance(error, commands.MissingRequiredArgument):
            message = f"{colorama.Fore.RESET}[{current_time}] {colorama.Fore.RED}[ERROR] {colorama.Fore.RESET}Missing a required argument: {error.param}"
        elif isinstance(error, commands.ConversionError):
            message = str(error)
        elif isinstance(error, commands.CommandNotFound):
            message = f"{colorama.Fore.RESET}[{current_time}] {colorama.Fore.RED}[ERROR] {colorama.Fore.RESET}Command not found"
        else:
            message = f"{colorama.Fore.RESET}[{current_time}] {colorama.Fore.RED}[ERROR] {colorama.Fore.RESET}Unable to debug"

        print(message)
    
    @bot.event
    async def on_command(ctx):
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        print(f"{colorama.Fore.RESET}[{current_time}] {colorama.Fore.RED}[Command] {colorama.Fore.RESET}{ctx.command.name}")

    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ini\n[utils] utilities\n[fun] fun stuff\n[encryption] encrypt stuff\n[activity] choose activity\n[crypto] check cryptocurrency prices\n[changelog] check updates\n\n[{watermark}]```", delete_after=8)

    @commands.command()
    async def changelog(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ini\n[changelog]\n\n[+] added changelog\n[+] added timezones\n[-] removed bugs\n\n[{watermark}]```", delete_after=8)

    @commands.command(aliases=["tools"])
    async def utils(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ini\n[ascii] (text)\n[online / offline] (no args)\n[cl] (ammount)\n[ping] no args\n[whois] (user)\n[lastMessage] (user)\n[timeNow] no args\n[convertTime] no args\n[spam] (ammount) (message)\n\n[{watermark}]```", delete_after=8)

    @commands.command()
    async def ascii(self, ctx, *, text: str = None):
        await ctx.message.delete()
        if text is None:
            await ctx.send(f"```ini\nInvalid argument\n\n[{watermark}]```", delete_after=8)
        else:
            f = Figlet(font='Slant')
            j = (f.renderText(text))
            try:
                await ctx.send(f"```{j}```", delete_after=20)
            except discord.HTTPException:
                try:
                    await ctx.send(f"```{j}```", delete_after=20)
                except Exception as e:
                    await ctx.send(f"Error: {e}", delete_after=8)

    @commands.command()
    async def pfp(self, ctx, member: discord.User = None):
        if not member:
            member = ctx.author
        await ctx.send(member.avatar_url)

    @commands.command()
    async def spam(self, ctx, amount: int, *, message):

        now = datetime.now()
        current_time = now.strftime("%H:%M")

        await ctx.message.delete()
        for i in range(0, amount):
            try:
                await ctx.send(message)
            except:
                continue
        
        await ctx.send(f"```ini\n[Function] Spam\n[Message] {message}\n[Amount] {amount}\n\n[{watermark}]```", delete_after=8)
        print(f"{colorama.Fore.RESET}[{current_time}] {colorama.Fore.RED}[Spam] {colorama.Fore.RESET}Spammed {amount} messages in {ctx.guild}")

    @commands.command()
    async def offline(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ini\nTMG is now offline\n\n[{watermark}]```", delete_after=8)
        sys.exit()

    @commands.command()
    async def clean(self, ctx):
        clear()
        lau()
        await ctx.message.delete()
        await ctx.send(f"```ini\n[Function] Clean\n[Target] Console\n\n[{watermark}]```", delete_after=8)

    @commands.command(aliases=["clear", "cls"])
    async def cl(self, ctx, amount: int):
        
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                await message.delete()
            except discord.Forbidden:
                try:
                    await message.delete()
                except discord.Forbidden:
                    pass
            except discord.HTTPException:
                await asyncio.sleep(10)
                await message.delete()
                
        await ctx.send(f"```ini\n[Function] Purge\n[Amount] {amount}\n\n[{watermark}]```", delete_after=8)
        print(f"{colorama.Fore.RESET}[{current_time}] {colorama.Fore.RED}[Clear] {colorama.Fore.RESET}Deleted {amount} messages in {ctx.guild}")

    # @commands.command()
    # async def lockgc(self, ctx, user = discord.Member):


    # @commands.command()
    # async def unlockgc(self, ctx, user = discord.Member):


    # @commands.command()
    # async def whitelist(self, ctx, user = discord.Member):

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()
        await ctx.send(f'```Ping: {round(self.bot.latency * 1000)}```')

    @commands.command()
    async def whois(self, ctx, *, user: discord.User = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        return await ctx.send("```ini\n[Registered] " + user.created_at.strftime(date_format) + f"\n[USER] {user.name}\n[ID] {user.id}\n\n[{watermark}]```", delete_after=8)

    @commands.command()
    async def moneyconvert(self, ctx, go, ammount, to):
        result = c.convert(ammount, go, to)

        await ctx.send(f"``{result}``")

    @commands.command()
    async def weightconvert(self, ctx, ammount: int, weight: str):
        if weight == 'KG':
            x = 'KG'
            y = 'LBS'
            kilograms = Kilograms(value=ammount)
            result = kilograms.to_pounds()
        elif weight == 'LBS':
            x = 'LBS'
            y = 'KG'
            pounds = Pounds(value=ammount)
            result = pounds.to_kilograms()

        await ctx.send(f"{ammount} {x} is ``{result}`` {y}")

    @commands.command()
    async def add(self, ctx, ammount: int, ammount2: int):
        await ctx.message.delete()
        answer = ammount + ammount2
        await ctx.send(answer)

    @commands.command()
    async def minus(self, ctx, ammount: int, ammount2: int):
        await ctx.message.delete()
        answer = ammount - ammount2
        await ctx.send(answer)

    @commands.command()
    async def times(self, ctx, ammount: int, ammount2: int):
        await ctx.message.delete()
        answer = ammount * ammount2
        await ctx.send(answer)

    @commands.command()
    async def divide(self, ctx, ammount: int, ammount2: int):
        await ctx.message.delete()
        answer = ammount / ammount2
        await ctx.send(answer)

    @commands.command()
    async def logall(self, ctx):
        await ctx.message.delete()

        with open('logs.json', 'r') as file:
            user_list = json.load(file)
        members = await ctx.guild.fetch_members(limit=150).flatten()
        for member in members:
            user_list.append(member.id)
        with open('logs.json', 'w') as file:
            json.dump(user_list, file)
        print('Logged All Users!')
        await ctx.send("Logged All Users!")

    @commands.command()
    async def lastMessage(self, ctx, users_id: int):
        await ctx.message.delete()
        oldestMessage = None
        for channel in ctx.guild.text_channels:
            fetchMessage = await channel.history().find(lambda m: m.author.id == users_id)
            if fetchMessage is None:
                continue

            if oldestMessage is None:
                oldestMessage = fetchMessage
            else:
                if fetchMessage.created_at > oldestMessage.created_at:
                    oldestMessage = fetchMessage

        if (oldestMessage is not None):
            await ctx.send(f"```ini\n[Message] {oldestMessage.content}\n\n[{watermark}]```", delete_after=8)
        else:
            await ctx.send(f"```ini\n[Error] no message found\n\n[{watermark}]```", delete_after=8)

    @commands.command()
    async def temp(self, ctx):
        await ctx.message.delete()
        def get_gpu_temperature():
            gpus = GPUtil.getGPUs()
            if gpus:
                return gpus[0].temperature
            return None

        gpu_temp = get_gpu_temperature()

        if gpu_temp:
            await ctx.send(f"```ini\n[GPU]\nTemp: {gpu_temp}°C\n\n[{watermark}]```")
        else:
            await ctx.send("Unable to retrieve GPU temperature.")

    @commands.command()
    async def specs(self, ctx):
        await ctx.message.delete()

        # CPU information
        cpu_processor = platform.processor()
        cpu_usage = psutil.cpu_percent()

        # RAM information
        ram = psutil.virtual_memory()
        ram_total = ram.total
        ram_available = ram.available

        # Disk information
        total, used, free = shutil.disk_usage('C:\\')  # Replace 'C' with the appropriate drive letter
        storage_total = total
        storage_used = used
        storage_free = free

        # GPU information
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            gpu_name = gpu.name
            gpu_memory = gpu.memoryTotal
            gpu_memoryused = gpu.memoryUsed
            gpu_memoryfree = gpu.memoryFree

        def get_cpu_name():
            command = "wmic cpu get name"
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            output, _ = process.communicate()
            output = output.decode("utf-8")
            lines = output.strip().split("\n")
            if len(lines) > 1:
                return lines[1].strip()
            return None

        def bytes_to_gb(bytes_value):
            gb_value = bytes_value / (1024 ** 3)  # 1024^3 bytes in a gigabyte
            return gb_value

        def mb_to_gb(mb_value):
            gb_value = mb_value / 1024  # 1 GB = 1024 MB
            return gb_value

        cpu_name = get_cpu_name()

        gpu_memory = mb_to_gb(gpu_memory)
        gpu_memoryused = mb_to_gb(gpu_memoryused)
        gpu_memoryfree = mb_to_gb(gpu_memoryfree)

        ram_total = bytes_to_gb(ram_total)
        ram_available = bytes_to_gb(ram_available)

        storage_total = bytes_to_gb(storage_total)
        storage_used = bytes_to_gb(storage_used)
        storage_free = bytes_to_gb(storage_free)

        os_name = platform.system()
        os_version = platform.release()

        await ctx.send(f"```ini\n[CPU Information]\nCPU: {cpu_name}\nCPU Processor: {cpu_processor}\nCPU Usage: {cpu_usage}\n\n[GPU Information]\nGPU: {gpu_name}\nGPU Memory: {math.ceil(gpu_memory)} GB\nGPU Memory Used: {math.ceil(gpu_memoryused)} GB\nGPU Memory Free: {math.ceil(gpu_memoryfree)} GB\n\n[RAM Information]\nRAM Ammount: {math.ceil(ram_total)} GB\nRAM Available: {math.ceil(ram_available)} GB\n\n[Storage Information]\nStorage Ammount: {math.ceil(storage_total)} GB\nStorage Used: {math.ceil(storage_used)} GB\nStorage Free: {math.ceil(storage_free)} GB\n\n[Operating System]\nOS: {os_name} {os_version}\n\n[{watermark}]```")

    @commands.command()
    async def timeNow(self, ctx):
        await ctx.message.delete()
        fmt = "%Y-%m-%d %H:%M:%S %Z%z"

        # Current time in UTC
        now_utc = datetime.now(timezone('UTC'))
        await ctx.send(now_utc.strftime(fmt) + " (UTC)", delete_after=8)

        # Convert to Europe/London time zone
        now_london = now_utc.astimezone(timezone('Europe/London'))
        await ctx.send(now_london.strftime(fmt) + " (London)", delete_after=8)

        # Convert to Europe/Berlin time zone
        now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
        await ctx.send(now_berlin.strftime(fmt) + " (Berlin)", delete_after=8)

        # Convert to CET time zone
        now_cet = now_utc.astimezone(timezone('CET'))
        await ctx.send(now_cet.strftime(fmt) + " (CET)", delete_after=8)

        # Convert to Israel time zone
        now_israel = now_utc.astimezone(timezone('Israel'))
        await ctx.send(now_israel.strftime(fmt) + " (Israel)", delete_after=8)

        # Convert to Canada/Eastern time zone
        now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
        await ctx.send(now_canada_east.strftime(fmt) + " (Canada/Eastern)", delete_after=8)

        # Convert to US/Central time zone
        now_central = now_utc.astimezone(timezone('US/Central'))
        await ctx.send(now_central.strftime(fmt) + " (US/Central)", delete_after=8)

        # Convert to US/Pacific time zone
        now_pacific = now_utc.astimezone(timezone('US/Pacific'))
        await ctx.send(now_pacific.strftime(fmt) + " (US/Pacific)", delete_after=8)

    @commands.command()
    async def convertTime(self, ctx, date_str):
        await ctx.message.delete()
        #date_str = "2009-05-05+22:28"
        datetime_obj = datetime.strptime(date_str, "%Y-%m-%d+%H:%M")

        fmt = "%Y-%m-%d %H:%M %Z%z"

        # Current time in UTC
        now_utc = datetime_obj.replace(tzinfo=timezone('UTC'))
        await ctx.send(now_utc.strftime(fmt) + " (UTC)", delete_after=8)

        # Convert to Europe/London time zone
        now_london = now_utc.astimezone(timezone('Europe/London'))
        await ctx.send(now_london.strftime(fmt) + " (London)", delete_after=8)

        # Convert to Europe/Berlin time zone
        now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
        await ctx.send(now_berlin.strftime(fmt) + " (Berlin)", delete_after=8)

        # Convert to CET time zone
        now_cet = now_utc.astimezone(timezone('CET'))
        await ctx.send(now_cet.strftime(fmt) + " (CET)", delete_after=8)

        # Convert to Israel time zone
        now_israel = now_utc.astimezone(timezone('Israel'))
        await ctx.send(now_israel.strftime(fmt) + " (Israel)", delete_after=8)

        # Convert to Canada/Eastern time zone
        now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
        await ctx.send(now_canada_east.strftime(fmt) + " (Canada/Eastern)", delete_after=8)

        # Convert to US/Central time zone
        now_central = now_utc.astimezone(timezone('US/Central'))
        await ctx.send(now_central.strftime(fmt) + " (US/Central)", delete_after=8)

        # Convert to US/Pacific time zone
        now_pacific = now_utc.astimezone(timezone('US/Pacific'))
        await ctx.send(now_pacific.strftime(fmt) + " (US/Pacific)", delete_after=8)

def setup(bot):
    bot.add_cog(Commands(bot))
