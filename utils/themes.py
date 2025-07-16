import json
import colorama

from utils import common

global theme

with open('config.json', 'r') as f:
    data = json.load(f)

theme = data["theme"]

def themeStartup():
    global theme

    if theme == "red":
        theme = colorama.Fore.RED
    elif theme == "blue":
        theme = colorama.Fore.BLUE
    elif theme == "yellow":
        theme = colorama.Fore.YELLOW
    elif theme == "white":
        theme = colorama.Fore.LIGHTBLACK_EX
    else:
        theme = colorama.Fore.RED

def themeChecker():
    global theme

    common.the()
    
    select = input(f"                                                      Choice: ")

    if select == "1":
        theme = colorama.Fore.RED
    elif select == "2":
        theme = colorama.Fore.BLUE
    elif select == "3":
        theme = colorama.Fore.YELLOW
    elif select == "4":
        theme = colorama.Fore.WHITE
    elif select == "5":
        theme = colorama.Fore.LIGHTBLACK_EX
    elif select == '6':
        common.clear()
    else:
        common.clear()
        themeChecker()
