import praw
import csv

from praw.models import MoreComments
reddit = praw.Reddit(client_id = 'xeG15Qt8cVfkaA' , client_secret= 'xLdWCwi3aunLoCvzXEPKvEdPj1U' , username = 'testreddit0', password = 'TestTest676' , user_agent = 'reddit_test')

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
