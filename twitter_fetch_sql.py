import sys
import time
import os
import tweepy

# make sure that the directory 'Tweets' exists, this is
# where the tweets will be archived
wdir = 'Tweets'
user = sys.argv[1]
id_file = user + '.csv'
timeline_file = user

if os.path.exists(wdir + '/' + id_file):
	f = open(wdir + '/' + id_file, 'r')
	since = int(f.read())
	f.close()
	tweets = tweepy.api.user_timeline(user, since_id=since)
else:
	tweets = tweepy.api.user_timeline(user)

if len(tweets) > 0:
	last_id = str(tweets[0].id)
	tweets.reverse()
	
	# write tweets to file
	f = open(wdir + '/' + timeline_file, 'a+')
	for tweet in tweets:
		output = str(tweet.created_at) + '|' + str(tweet.id_str) + '|' +  tweet.user.location.encode('utf-8')  + '|' + user + '|' +  tweet.text.replace('\r', ' ').encode('utf-8') + '|' + tweet.source.encode('utf-8') + '\n'
		f.write(output)
		print output
	f.close()

	# write last id to file
	f = open(wdir + '/' + id_file, 'w')
	f.write(last_id)
	f.close()
else:
	print 'No new tweets for ' + user