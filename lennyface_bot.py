#!/usr/bin/python
import time
import praw
from login import *

r = praw.Reddit(user_agent ="lennyface reply bot by u/ccviper")
r.login(USERNAME, PASSWORD)

subreddit = r.get_subreddit("funny")

replied = []

def replybot():
   
    comments = subreddit.get_comments(limit=1000)
    phrase = "( ͡° ͜ʖ ͡°)"
    
    for comment in comments:        
        comment_body = comment.body.lower()        
        if phrase in comment_body and comment.id not in replied:
            comment.reply("( ͡~ ͜ʖ ͡°)")            
            replied.append(comment.id)
            
        else:
            continue

 while True:
    replybot()
    time.sleep(5)