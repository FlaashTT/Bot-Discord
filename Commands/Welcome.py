#Comamdo para ativar Emded
from turtle import color, title
#Importação do Discord
import discord
#Importação para os comandos na linhas
from discord.ext import commands

#Comando de Prefixo geral
client= commands.Bot(command_prefix = ' . ')
class Meu(discord.client):
    @client.event
    #Comando de mensagem
    async def on_message(message):
        #Comando Se a resposta for »hello
        if message.content.startswith('.hello'):
            #Comando onde o Bot envia
            await message.channel.send('Hello')
            return

    @client.event
    #Comando quando uma pessoa entra
    async def on_member_join(member):
        #criacao de um emblema
        embed = discord.Embed(title='Bem Vindo ao TeamDX! {member.mention}',color=0x9208ea,description=f'Obrigado por entrares no Servidor')
        #Ip de comando do Servidor
        guild = client.get_guild('428975980531417091')
        #Ip de comando do Canal onde Deseja  
        channel = client.get_channel('428975980988858368')
        #Comando Externo para o Membro
        await client.send(' Alguma questão ao seu dispor entre em contacto com {guild.name},{member.name}')
        return
          