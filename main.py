import os
import command_handler
import discord
from dotenv import load_dotenv

from command_handler import command_handler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()
cmd = command_handler()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! {os.name}')


@client.event
async def on_message(message):
    if message.author == client.user:
      return
    message.content  = str(message.content).upper()

    if message.content == '!COMMANDS':
        response = cmd.get_list_commands()
        await message.channel.send(response)

    if '!MEME' in str(message.content)[0:5]:
        
        cmd_sub = str(message.content).split(" ")
        
        if len(cmd_sub)==2:
            response = (cmd.get_meme(cmd_sub[1])).split('|')
        elif len(cmd_sub)==3:
            response = (cmd.get_meme(cmd_sub[1],cmd_sub[2])).split('|')      
        else:
            response = (cmd.get_meme()).split('|')
        
        await message.channel.send(response[0] + "\n" + response[1])
    
    if "!JIRA" in message.content:
        
        args = str(message.content).replace("!JIRA ","").split(" ")
        cmd_1 = args[0]
        body = args[1]
        
        import jira_handler
        jira = jira_handler.jira_handler()
        
        response = jira.cmd_handler(cmd_1,body)
        
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