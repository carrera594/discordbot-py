
import praw 
import os
import random

client_id = os.getenv('client_id')
client_secret=os.getenv('client_secret')
praw_password=os.getenv('praw_password')
username=os.getenv('praw_username')

reddit = praw.Reddit(
                        client_id=client_id,
                        client_secret=client_secret, 
                        password=praw_password,
                        user_agent='bot1', 
                        username=username
                    )

subreddit = reddit.subreddit('dankmemes')
images = {}
i = 0
#Download Images from Reddit
for submission in subreddit.hot(limit=int(20)):
    titleOfSubmission = submission.title
    isStickied = submission.stickied
    fullURL = submission.url
    fileExtension = submission.url.rsplit('.',1)
    isNSFW = submission.over_18
    
    if( not isStickied):
        images[i] = {   
                        "Title":titleOfSubmission,
                        "URL":fullURL,
                        "isNSFW":isNSFW
                    }
        i=i+1
        print(fullURL)

rand = random.randint(0,20)
print(images[rand]["Title"])