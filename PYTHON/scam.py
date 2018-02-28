import praw
from praw_creds import client_id, client_secret, password, user_agent, username

reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret, password=password,
                    user_agent=user_agent, username=username)

def find_spam_by_name(search_query):
    authors = []
    for submission in reddit.subreddit("all").search()
