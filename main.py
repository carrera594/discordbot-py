from datetime import datetime
import os
import command_handler
import discord
import logging,pathlib
from dotenv import load_dotenv

from command_handler import command_handler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

today = datetime.now()
DATE_FORMAT = today.strftime('%Y-%m-%d')

ROOT_DIRECTORY = str(pathlib.Path(__file__).parent.absolute())
logging.basicConfig(filename=ROOT_DIRECTORY+'/LOGS/logging.log'.format(DATE_FORMAT),encoding='utf-8',level=logging.INFO)

client = discord.Client()
cmd = command_handler()

def get_current_time():
    return str(datetime.now().strftime("%Y-%m-%d_%H_%M_%S"))


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! {os.name}')


@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return
        message.content  = str(message.content).upper()

        logging.info(get_current_time()+": "+str(message.author)+" has requested "+str(message.content))
        if message.content == '!COMMANDS':
            response = cmd.get_list_commands()
            await message.channel.send(response)
        elif '!MEME' in str(message.content)[0:5]:
            cmd_sub = str(message.content).split(" ")
            if len(cmd_sub)==2:
                response = (await cmd.get_meme(cmd_sub[1])).split('|')
            elif len(cmd_sub)==3:
                response = (await cmd.get_meme(cmd_sub[1],cmd_sub[2])).split('|')      
            else:
                response =  (await cmd.get_meme()).split('|')
            await message.channel.send(response[0] + "\n" + response[1])
        elif "!JIRA" in message.content:
            args = str(message.content).replace("!JIRA ","").split(" ")
            cmd_1 = args[0]
            body = args[1]
            
            import jira_handler
            jira = jira_handler.jira_handler()
            response = jira.cmd_handler(cmd_1,body)
            await message.channel.send(response) 
        elif "!HELP" in message.content:
            response = cmd.answer_question(str(message.content).replace("!HELP ",""))
            await message.channel.send(response) 

        elif "!TEXT" in message.content:
            response = cmd.friend_prompt(str(message.content).replace("!TEXT ",""))
            await message.channel.send(response) 

        elif "!MARV" in message.content:
            response = cmd.sarcasm_response(str(message.content).replace("!TEXT ",""))
            await message.channel.send(response) 

        elif message.content == '!99':
            response = cmd.return_brooklyn99_quote()
            await message.channel.send(response) 
        
        elif message.content.upper() == "!COLLIN":
            await message.channel.send("Collin smells") 

        elif message.content.upper() == "!ALAN":
            response = cmd.get_alan_prompt()
            await message.channel.send(response) 

        elif '!' in str(message.content)[0:1]:
            await message.channel.send("Unsupported Command")
        
    except:

        await message.channel.send("Program Exception has Occurred.") 


client.run(TOKEN)