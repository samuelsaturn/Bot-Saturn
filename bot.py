from discord import app_commands
from discord.ext import commands
from key import token
import discord
from discord import app_commands

id_do_servidor =  1072703415060267148

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = token.get('TOKEN')

@client.event
async def on_message(message):

    conteudo = message.content
    l_conteudo = conteudo.lower()

    if message.author == client.user:
        return
    
    if l_conteudo.startswith("!taporra"):
        await message.channel.send(f'taporraaaaaaa {message.author}') 

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'taporra', description='Testando') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://img.ifunny.co/images/53490638f7ab9318dc70caa3cb5693c6e463afc8391472b9bba782ef113b902a_1.jpg", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'eita', description='eitaaaaaa')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://cdn.discordapp.com/attachments/1009900762362548264/1042590621736652971/1668445755369377.webm", ephemeral = False)     

aclient.run(TOKEN)