import os

import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

chat = GenericAssistant()
client = discord.Client()
load_dotenv()

TOKEN = os.getenv('MTEyNjUxNzAwNzA5ODA2NTAwOA.G-qFZs.BugMyWCcZRY9HZASFYRYWYpjyJ_SVJPQHjm9Zs')
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.starswitch("!hello"):
        pass


client.run(TOKEN)




