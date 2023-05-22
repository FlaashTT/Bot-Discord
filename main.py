#Importação do Discord
import discord
#Importação para os comandos na linhas
from Meu import *

#Comando de Prefixo geral
client=commands.Bot(command_prefix = '.')

@client.event
#Comando para corresponder ao bot que esta Pronto
async def on_ready():
    #Comando de enviar a partir do Lider
    print('===============')
    print('Online {0.user}'.format(client))
    print('===============')
    
#Comando de Chave do Bot
client.run('')