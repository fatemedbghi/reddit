import praw
import csv
import datetime

reddit = praw.Reddit(
    client_id='fSitnrFQDi472RqYl2N8tg',
    client_secret='Rqd5jrh_l_QJk0bREmHihx3P9y9OdA',
    user_agent='YOUR_USER_AGENT',
)

subreddit_name = 'politics'
start_time = datetime.datetime(2023, 1, 1).timestamp()
post_limit = None  

subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.new(limit=post_limit)

data = []
for post in posts:
    if start_time <= post.created_utc:
        post_data = {
            'score': post.score,
            'num_comments': post.num_comments,
            'created_utc': post.created_utc,
            'author': post.author.name if post.author else None,
            'is_self': post.is_self,
        }

        data.append(post_data)

csv_filename = 'politics_data.csv'
csv_columns = ['score', 'num_comments', 'created_utc', 'author', 'is_self']

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(data)