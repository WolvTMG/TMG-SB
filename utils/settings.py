import os
import sys
import json
import time
import discord
import colorama
from os.path import exists
from discord.ext import commands
from discord.ext.commands import Bot

from utils.common import *

with open('config.json', 'r') as f:
    data = json.load(f)

watermark = data["watermark"]

def watermarkStartup():
    global watermark

    if watermark == '':
        watermark = 'TMG - MIDVITE'

def chooseWatermark():
    global watermark

    con()

    select = input(f"                                                 Rename watermark: ")
    watermark = select
    clear()

def ConfigSet():

    con()

    select = input(
        f"                                                      Choice: ")

    if select == "1":
        clear()
        ConfigSet()
    elif select == "2":
        clear()
        ConfigSet()
    elif select == "3":
        clear()
        chooseWatermark()
    elif select == "4":
        clear()
        ConfigSet()
    elif select == "5":
        clear()
        ConfigSet()
    elif select == '6':
        clear()
    else:
        clear()
        ConfigSet()
