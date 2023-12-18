import praw
import csv
import datetime

reddit = praw.Reddit(
    client_id='fSitnrFQDi472RqYl2N8tg',
    client_secret='Rqd5jrh_l_QJk0bREmHihx3P9y9OdA',
    user_agent='YOUR_USER_AGENT',
)

subreddit_name = 'OpenAI'
start_time = datetime.datetime(2022, 1, 1).timestamp()
end_time = datetime.datetime(2024, 1, 1).timestamp() 
post_limit = None  

subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.new(limit=post_limit)

data = []
for post in posts:
    if start_time <= post.created_utc <= end_time:
        post_data = {
            'id': post.id,
            'title': post.title,
            'score': post.score,
            'ups': post.ups,
            'downs': post.downs,
            'num_comments': post.num_comments,
            'created_utc': post.created_utc,
            'selftext': post.selftext,
            'url': post.url,
            'author': post.author.name if post.author else None,
            'subreddit': post.subreddit.display_name,
            'stickied': post.stickied,
            'is_self': post.is_self,
            'over_18': post.over_18,
            'locked': post.locked,
            'spoiler': post.spoiler,
            'permalink': post.permalink,
        }

        data.append(post_data)

csv_filename = 'reddit_data.csv'
csv_columns = ['id', 'title', 'score', 'ups', 'downs', 'num_comments', 'created_utc', 'selftext', 'url', 'author', 'subreddit', 'stickied', 'is_self', 'over_18', 'locked', 'spoiler', 'permalink']

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(data)