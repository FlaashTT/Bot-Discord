#Importação do Discord
import discord
#Importação para os comandos na linhas
from discord.ext import commands

#Comando de Prefixo geral
client= commands.Bot(command_prefix = '.')

@client.event
#Comando de mensagem
async def on_message(message):
    #Comando Se em resposta for »help
    if message.content.startswith('.help'):
        #Comando onde o Bot envia
        await message.channel.send(
            '•hello\n'
            '•help\n'
            '•play\n'
        )
        return