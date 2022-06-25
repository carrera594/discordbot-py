import os
import command_handler
import discord
from dotenv import load_dotenv

from command_handler import command_handler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN_DEV')


client = discord.Client()
cmd = command_handler()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! {os.name}')


@client.event
async def on_message(message):


    if message.author == client.user:
      return

    if message.content == '!COMMANDS':
        response = cmd.get_list_commands()
        await message.channel.send(response)

    if "!HELP" in message.content:
        response = cmd.answer_question(str(message.content).replace("!HELP ",""))
        await message.channel.send(response) 

    if "!TEXT" in message.content:
        response = cmd.friend_prompt(str(message.content).replace("!TEXT ",""))
        await message.channel.send(response) 

    if "!MARV" in message.content:
        response = cmd.sarcasm_response(str(message.content).replace("!TEXT ",""))
        await message.channel.send(response) 

    if message.content == '!99':
        response = cmd.return_brooklyn99_quote()
        await message.channel.send(response) 
    
    if message.content.upper() == "!COLLIN":
        await message.channel.send("Collin smells") 

    if message.content.upper() == "!ALAN":
        response = cmd.get_alan_prompt()
        await message.channel.send(response) 


client.run(TOKEN)