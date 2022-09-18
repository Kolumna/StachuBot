import discord
import os

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('Zostałeś zalogowany jako {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('%elo'):
        await message.channel.send('No elo!')


client.run(os.environ['TOKEN'])
