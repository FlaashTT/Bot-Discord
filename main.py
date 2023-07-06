import os

import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

chat = GenericAssistant()
client = discord.Client()
load_dotenv()

TOKEN = os.getenv('')
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.starswitch("!hello"):
        pass


client.run(TOKEN)




