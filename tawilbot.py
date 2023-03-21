import settings
from discord.ext import commands
from discord import Intents
from discord import Embed

from bs4 import BeautifulSoup as bs
import requests
from datetime import date
import pandas as pd
import json
import time

import re


prefix = settings.PREFIX
intents = Intents.default()
#intents.message_content = True
intents.messages = True
bot = commands.Bot(intents=intents,command_prefix=prefix)




#tawil user id: 187718098743328768
@bot.event
async def on_ready():
    print("Everything's all ready to go~")







bot.run(settings.TOKEN)