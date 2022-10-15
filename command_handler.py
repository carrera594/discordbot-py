from pickle import TRUE
import random
import os
from warnings import catch_warnings
import openai
import os
import file_handler
import random
import sys 
import asyncpraw
import configparser


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
fh = file_handler.fileHandler()

is_windows = sys.platform.startswith('win')
path = "\\" if is_windows else "/"

class command_handler:
    
    

    def __init__(self):
        return

    def get_list_commands(self):
        return fh.load_file_str(f"{ROOT_DIR}{path}DATA{path}!Commands.txt")

    def return_brooklyn99_quote(self):
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]
        return random.choice(brooklyn_99_quotes)

    

    def get_alan_prompt(self):
        arr = fh.load_file_arr(f"{ROOT_DIR}{path}DATA{path}AlanPrompts.txt")
        return arr[random.randint(0, len(arr)-1)]

    def open_ai(self,model="text-davinci-002",uprompt="",temperature=0.5,max_tokens=60,top_p=0.3,frequency_penalty=0.5,presence_penalty=0.0,METHOD=""):
        try:
            response = openai.Completion.create(
                model=model,
                prompt=uprompt,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty
            )

            responseTxt = response["choices"][0]["text"]
        except:
            responseTxt = f"Unable to process.. !{METHOD}"

        if(responseTxt==''):
            responseTxt = f"Empty Response.. !{METHOD}"

        return responseTxt

    def answer_question(self, msg):

        uprompt = (fh.load_file_str(f"{ROOT_DIR}{path}DATA{path}AnswerQuestion.txt")).replace("USER_INPUT",msg)
        return self.open_ai("text-davinci-002",uprompt,0.9,100,1,0.0,0.0,"HELP")

    def friend_prompt(self, msg):
        
        uprompt = (fh.load_file_str(f"{ROOT_DIR}{path}DATA{path}FriendPrompt.txt")).replace("USER_INPUT",msg)
        return self.open_ai("text-davinci-002",uprompt,0.9,60,1,0.5,0.0,"TEXT")

    def sarcasm_response(self, msg):
        uprompt = (fh.load_file_str(f"{ROOT_DIR}{path}DATA{path}SarcasmPrompt.txt")).replace("USER_INPUT",msg)
        return self.open_ai("text-davinci-002",uprompt,0.9,60,0.3,0.5,0.0,"MARV")
    
    
    async def get_meme(self, subreddit="dankmemes", limit=20):
        
        reddit_limit = int(os.getenv("reddit_limit"))
        limit = int(limit)
        
        if(limit<0):
            return "Limit cannot be less than 0!|"
        elif(limit>=reddit_limit):
            return f"Limit cannot exceed {limit}.|"
        
        
        client_id = os.getenv('client_id')
        client_secret=os.getenv('client_secret')
        praw_password=os.getenv('praw_password')
        username=os.getenv('praw_username')

        try:
            reddit = asyncpraw.Reddit(
                                    client_id=client_id,
                                    client_secret=client_secret, 
                                    password=praw_password,
                                    user_agent='bot1', 
                                    username=username
                                )
            

            subreddit = await reddit.subreddit(subreddit)
            
            images = {}
            i = 0
            #Download Images from Reddit
            async for submission in subreddit.hot(limit=int(limit)):
                titleOfSubmission = submission.title
                isStickied = submission.stickied
                fullURL = submission.url
                isNSFW = submission.over_18
                
                if( not isStickied ):
                    images[i] = {   
                                    "Title":titleOfSubmission,
                                    "URL":fullURL,
                                    "isNSFW":isNSFW
                                }
                    i=i+1
                    #print(fullURL)

            rand = random.randint(0,20)
            return images[rand]["Title"] + "|" + images[rand]["URL"]
        except:
            return "Subreddit not found.|"