import praw
import csv
import os
from praw.models import MoreComments
reddit = praw.Reddit(client_id = os.environ["CLIENT_ID"], client_secret= os.environ["CLIENT_SECRET"] , username = os.environ["USERNAME"], password = os.environ["PASSWORD"] , user_agent = os.environ["USER_AGENT"])

subreddit = reddit.subreddit('python')
hot_python = subreddit.hot(limit=5)
five_comments = subreddit.comments(limit=3)
submission_id = reddit.submission(id='3g1jfi')
#submission_id.replace_more(limit=None, threshold=0)
#for submission in hot_python:
#	print(submission.title)
number = 0
#for comment in five_comments:
#	print("Comment")
#	number += 1
#	print(number)
#	print(comment.body)


with open('output.csv', 'w', newline='') as f:
	thewriter = csv.writer(f)
	#thewriter.writerow(top_level_comment.body)
	for top_level_comment in submission_id.comments:
		if isinstance(top_level_comment, MoreComments):
			continue
		print("#######")
		print(top_level_comment.body)
		thewriter.writerow([top_level_comment.body])
#	with open('output.csv', 'w', newline='') as f:
#		thewriter = csv.writer(f)
#		thewriter.writerow([top_level_comment.body])
