import os
import praw
import datetime
import sys
import json
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ['CLIENT_ID'],
    client_secret=os.environ['CLIENT_SECRET'],
    user_agent="reddit-flair-analyzer",
)

SUB=sys.argv[1]
NUM_POSTS=sys.argv[2]
subreddit = reddit.subreddit(SUB)
posts_without_flair = []

for submission in subreddit.new(limit=int(NUM_POSTS)):
    dt = datetime.datetime.fromtimestamp(submission.created)

    if not submission.link_flair_text:
        posts_without_flair.append({
            "created": str(dt),
            "flair": submission.link_flair_text,
            "title": submission.title,
        })

# print(json.dumps(posts_without_flair))
print(tabulate(posts_without_flair, headers="keys"))
