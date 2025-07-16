import sys
import json
import math
import psutil
import GPUtil
import shutil
import asyncio
import discord
import platform
import subprocess
from colorama import Fore
from pytz import timezone
from pyfiglet import Figlet
import discord.ext.commands
from datetime import datetime, date, time
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
        await ctx.send(f"""```ini
[utils] utilities
[fun] fun stuff
[encryption] encrypt stuff
[activity] choose activity
[crypto] check cryptocurrency prices
[changelog] check updates
\n[{watermark}]```""", delete_after=8)

    @commands.command()
    async def changelog(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"""```ini
[changelog]
                       
[+] added changelog
[+] added timezones
[+] added missing commands to help
[+] fixed timezones
[+] cleaned up some errors
[-] removed bugs
\n[{watermark}]```""", delete_after=8)

    @commands.command(aliases=["tools"])
    async def utils(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"""```ini
[ascii] (text)
[offline] (no args)
[cl] (ammount)
[clean] no args
[ping] no args
[whois] (user)
[specs] no args
[timeNow] no args
[convertTime] (time)
[spam] (ammount) (message)
[moneyConvert] (currency -> amount -> currency)
[weightConvert] (amount) (kg/lbs)
[add] (amount) (amount)
[minus] (amount) (amount)
[times] (amount) (amount)
[divide] (amount) (amount)
\n[{watermark}]```""", delete_after=8)

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
        return await ctx.send(f"""```ini
[Registered] """ + user.created_at.strftime(date_format) + f"""
[USER] {user.name}
[ID] {user.id}
\n[{watermark}]```""", delete_after=8)

    @commands.command()
    async def moneyConvert(self, ctx, go, ammount, to):
        go = go.upper()
        to = to.upper()
        result = c.convert(ammount, go, to)

        await ctx.send(f"```ini\n{ammount} {go} is equal to [{result}] {to}```")

    @commands.command()
    async def weightConvert(self, ctx, ammount: int, weight: str):
        weight = weight.upper()
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

        await ctx.send(f"```ini\n{ammount} {x} is [{result}] {y}```")

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

    # @commands.command()
    # async def logall(self, ctx):
    #     await ctx.message.delete()

    #     with open('logs.json', 'r') as file:
    #         user_list = json.load(file)
    #     members = await ctx.guild.fetch_members(limit=150).flatten()
    #     for member in members:
    #         user_list.append(member.id)
    #     with open('logs.json', 'w') as file:
    #         json.dump(user_list, file)
    #     print('Logged All Users!')
    #     await ctx.send("Logged All Users!")

    @commands.command()
    async def gpuTemp(self, ctx):
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

        def bytes_to_gb(val): return val / (1024 ** 3)
        def mb_to_gb(val): return val / 1024

        cpu_name = subprocess.check_output("wmic cpu get name", shell=True).decode().split("\n")[1].strip()
        cpu_processor = platform.processor()
        cpu_usage = psutil.cpu_percent()

        ram = psutil.virtual_memory()
        ram_total = bytes_to_gb(ram.total)
        ram_available = bytes_to_gb(ram.available)

        total, used, free = shutil.disk_usage('C:\\')
        storage_total = bytes_to_gb(total)
        storage_used = bytes_to_gb(used)
        storage_free = bytes_to_gb(free)

        gpus = GPUtil.getGPUs()
        gpu_info = []
        for gpu in gpus:
            gpu_info.append(
                f"{gpu.name} ({math.ceil(mb_to_gb(gpu.memoryUsed))} / {math.ceil(mb_to_gb(gpu.memoryTotal))} GB used)"
            )

        os_name = platform.system()
        os_version = platform.release()

        msg = f"""```ini
[CPU Information]
CPU Name: {cpu_name}
CPU Processor: {cpu_processor}
CPU Usage: {cpu_usage}%

[GPU Information]
""" + "\n".join(f"GPU: {g}" for g in gpu_info) + f"""

[RAM Information]
RAM Total: {math.ceil(ram_total)} GB
RAM Available: {math.ceil(ram_available)} GB

[Storage Information]
Storage Total: {math.ceil(storage_total)} GB
Storage Used: {math.ceil(storage_used)} GB
Storage Free: {math.ceil(storage_free)} GB

[Operating System]
OS: {os_name} {os_version}

[{watermark}]
```"""
        
        await ctx.send(msg)

    @commands.command()
    async def timeNow(self, ctx):
        await ctx.message.delete()

        fmt = "%H:%M"
        now_utc = datetime.now(timezone('UTC'))

        zones = {
            "UTC": "UTC",
            "Europe/London": "London",
            "Europe/Berlin": "Berlin",
            "CET": "CET",
            "Israel": "Israel",
            "Canada/Eastern": "Canada",
            "US/Central": "US Central",
            "US/Pacific": "US Pacific"
        }

        lines = []
        for tz_name, label in zones.items():
            local_time = now_utc.astimezone(timezone(tz_name)).strftime(fmt)
            lines.append(f"It is currently [{local_time}] in {label}")

        await ctx.send(f"```ini\n" + "\n".join(lines) + "```")

    @commands.command()
    async def convertTime(self, ctx, time_input: str):
        await ctx.message.delete()

        fmt = "%H:%M"
        try:
            today = date.today()

            input_time = datetime.strptime(time_input, fmt).time()
            naive_dt = datetime.combine(today, input_time)

            london_tz = timezone('Europe/London')
            london_time = london_tz.localize(naive_dt)

            timezones = {
                "UTC": timezone('UTC'),
                "Berlin": timezone('Europe/Berlin'),
                "CET": timezone('CET'),
                "Israel": timezone('Israel'),
                "Canada": timezone('Canada/Eastern'),
                "US Central": timezone('US/Central'),
                "US Pacific": timezone('US/Pacific'),
            }

            results = [f"[{london_time.strftime(fmt)}] in London (input)"]
            for name, tz in timezones.items():
                converted_time = london_time.astimezone(tz).strftime(fmt)
                results.append(f"[{converted_time}] in {name}")

            await ctx.send(f"```ini\n" + "\n".join(results) + "```")

        except ValueError:
            await ctx.send("Please enter the time in HH:MM format (e.g. `15:30`).")

def setup(bot):
    bot.add_cog(Commands(bot))
