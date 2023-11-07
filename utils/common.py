import os
import sys
import json
import time
import discord
import colorama
from os.path import exists
from discord.ext import commands

from utils import themes


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def SlowPrint(_str):
    for letter in _str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

with open('config.json', 'r') as f:
    data = json.load(f)

token = data["token"]
prefix = data["prefix"]

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

def tmg():  
    global theme
    txt = f"Logged in as {bot.user.name} (ID: {bot.user.id} )"
    log = txt.center(120)

    print(themes.theme + f"""
                            ████████╗███╗   ███╗ ██████╗               ███████╗██████╗ 
                            ╚══██╔══╝████╗ ████║██╔════╝               ██╔════╝██╔══██╗
                               ██║   ██╔████╔██║██║  ███╗    █████╗    ███████╗██████╔╝
                               ██║   ██║╚██╔╝██║██║   ██║    ╚════╝    ╚════██║██╔══██╗
                               ██║   ██║ ╚═╝ ██║╚██████╔╝              ███████║██████╔╝
                               ╚═╝   ╚═╝     ╚═╝ ╚═════╝               ╚══════╝╚═════╝ 
                                                           

                                                 Made by {colorama.Fore.RESET}WolvTMG """ + themes.theme + f"""
{log}
                                                                                                (Prefix: {prefix} )
                                                                                                (Guild Count: {len(bot.guilds)} )
                        [1] Start Script | [2] Update       | [3] Join Discord | [4] Threads
                        [5] Logs         | [6] Coming soon  | [7] Coming soon  | [8] Clear
                        [9] Themes       | [10] Update Log  | [11] Config      | [12] Exit

        """)

def lau():
    global theme
    txt = f"Logged in as {bot.user.name} (ID: {bot.user.id} )"
    log = txt.center(120)

    print(themes.theme + f"""
                            ████████╗███╗   ███╗ ██████╗               ███████╗██████╗
                            ╚══██╔══╝████╗ ████║██╔════╝               ██╔════╝██╔══██╗
                               ██║   ██╔████╔██║██║  ███╗    █████╗    ███████╗██████╔╝
                               ██║   ██║╚██╔╝██║██║   ██║    ╚════╝    ╚════██║██╔══██╗
                               ██║   ██║ ╚═╝ ██║╚██████╔╝              ███████║██████╔╝
                               ╚═╝   ╚═╝     ╚═╝ ╚═════╝               ╚══════╝╚═════╝

                                                 Made by {colorama.Fore.RESET}WolvTMG """ + themes.theme + f"""
{log}            
                                                                                                (Prefix: {prefix} )
                                                                                                (Guild Count: {len(bot.guilds)} )
                                                                
        """)

def the():
    print("""
                              ████████╗██╗  ██╗███████╗███╗   ███╗███████╗███████╗
                              ╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔════╝██╔════╝
                                 ██║   ███████║█████╗  ██╔████╔██║█████╗  ███████╗
                                 ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══╝  ╚════██║
                                 ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗███████║
                                 ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝

                                [1] Original     | [2] Blue         | [3] Yellow
                                [4] White        | [5] Black        | [6] Exit



        """)

def con():
    print(f"""
                                     ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ 
                                    ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝ 
                                    ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
                                    ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
                                    ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
                                     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ 

                                [1] Change token    | [2] Change prefix  | [3] Change Watermark
                                [4] Coming soon     | [5] Coming soon    | [6] Exit



       """)
