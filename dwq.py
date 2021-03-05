import requests
import discord
from discord.ext import commands
client = commands.Bot( command_prefix= '!')
@client.event

async def on_ready():
    print('Клоун на месте.')

@client.command( pass_context = True)

async def ржака(ctx):
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=ru&amp;type=json").text

    print(response)
    await ctx.send(response)

client.run("token")
