# TMG SB was proudly coded by WolvTMG (https://github.com/WolvTMG)
# Copyright (c) 2022 WolvTMG | https://tmgmidvite.com
# TMG SB under the GNU General Public Liscense v2 (1991)

import os
import sys
import time
import discord
import colorama
import threading
from PIL import Image
from _thread import *
from os.path import exists
from pyfiglet import Figlet
from datetime import datetime
from discord.ext import commands
from win10toast import ToastNotifier
from discord.ext.commands import Bot
from colorama import Fore, Back, Style
from unittest.util import _count_diff_all_purpose
from discord.ext.commands import has_permissions, MissingPermissions

from utils.common import *
from utils.themes import *
from utils.update import *
from utils.settings import *

global counter

colorama.init()

now = datetime.now()
current_time = now.strftime("%H:%M")

threads = []
toast = ToastNotifier()
counter = 0

def main():
    
    intents = discord.Intents().default()
    intents.members = True
    client = discord.Client(intents=intents)

    threads = threading.active_count()

    SlowPrint("Booting TMG SB\n")
    time.sleep(1.0)
    SlowPrint("Made by WolvTMG")
    time.sleep(1.0)
    clear()
    themeStartup()

    def load():
        for filename in os.listdir('./cogs'):
            if filename.endswith(".py"):
                bot.load_extension(f'cogs.{filename[:-3]}')
                
    def menu():
        global theme
        global counter

        if counter <= 0:
            SlowPrint("Loading ...")
            time.sleep(2.5)
            clear()
            counter = counter + 1
    
        tmg()  

        select = input("                                                      Choice: ")

        if select == '1':
            load()
            clear()
            lau()
            print(f"{colorama.Fore.RESET}[{current_time}] {colorama.Fore.RED}[TMG-SB] {colorama.Fore.RESET}has been launched\n")
        elif select == '2':
            clear()
            lau()
            e = input("[Update] No updates yet\n\n[Enter] to return")
            clear()
            menu()
        elif select == '3':
            clear()
            lau()
            e = input(".gg/uYCeDP3\n\n[Enter] to return")
            clear()
            menu()
        elif select == '4':
            clear()
            lau()
            e = input(f"{threads}\n\n[Enter] to return")
            clear()
            menu()
        elif select == '5':
            clear()
            menu()
        elif select == '6':
            clear()
            menu()
        elif select == '7':
            clear()
            menu()
        elif select == '8':
            clear()
            menu()
        elif select == '9':
            clear()
            themeChecker()
            clear()
            menu()
        elif select == '10':
            clear()
            lau()
            e = input("\n[Update] Changelog 4/4/2022, nothing yet\n\n[Enter] to return")
            clear()
            menu()
        elif select == '11':
            clear()
            ConfigSet()
            clear()
            menu()
        elif select == '12':
            os._exit(1)
        else:
            clear()
            menu()

    process = threading.Thread(target=menu)
    process.start()

    try:
        bot.run(token, bot=False)
    except discord.LoginFailure:
        clear()
        print('Invalid Token')
        time.sleep(6)

main()

# TMG SB was proudly coded by WolvTMG (https://github.com/WolvTMG)
# Copyright (c) 2022 WolvTMG | https://tmgmidvite.com
# TMG SB under the GNU General Public Liscense v2 (1991)
