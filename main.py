import discord
import logging

import db

handle = '$'

logging_handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(handle + 'register'):
        if db.does_user_exist(message.author.id) is False:
            db.create_user(message.author.id)
            await message.channel.send('Registered! >w<')
        else:
            await message.channel.send('You are already registered! Silly! :3')




client.run('', log_handler=logging_handler)