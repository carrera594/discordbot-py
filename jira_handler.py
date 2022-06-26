import os
import file_handler
import sys
import requests
import json

class jira_handler:
    
    def __init__(self):
        return
    
    def get_issue(self,id):
        print()
        

        url = "https://billforce.atlassian.net/rest/api/2/issue/"+id

        payload={}
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic '+os.getenv('jira_auth')
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        
    
    def cmd_handler(self,cmd,body):
        
        if(cmd=="GET"):
            url = "https://billforce.atlassian.net/rest/api/2/issue/"+body

            payload={}
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic '+os.getenv('jira_auth')
            }

            response = requests.request("GET", url, headers=headers, data=payload).json()
            
            key             = body
            summary         = response["fields"]["summary"]
            description     = response["fields"]["description"]
            priority        = response["fields"]["priority"]["name"]
            created         = response["fields"]["created"]
            assignee        = "Unassigned" if response["fields"]["assignee"]==None else response["fields"]["assignee"]["displayName"]
            reporter        = response["fields"]["reporter"]["displayName"]

            response_body = ("Key: {}\nTitle: {}\nDescription: {}\nPriority: {}\nAssignee: {}\nReporter: {}\nCreated: {}".format(key,summary,description,priority,assignee,reporter,created))

            return '```'+str(response_body)+'```'