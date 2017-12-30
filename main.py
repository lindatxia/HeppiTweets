from twitter import *
from TwitterSearch import *
import json
from random import randint
import time
with open('config.json') as data: 
	data = json.load(data)


consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token = data["access_token"]
access_secret = data["access_secret"]

# Connects to the Twitter Search Python Wrapper API
def getTweetList():
	tweetList = []
	try:

		tso = TwitterSearchOrder() 
		tso.set_keywords(['Blessed','Happy', 'Surprise', 'Love', '-:('],or_operator = True)
		tso.add_keyword('happy')
		tso.set_language('en') 
		tso.set_include_entities(False) 
		tso.set_positive_attitude_filter()
		tso.remove_link_filter()
		querystr = tso.create_search_url()

		tso.set_search_url(querystr + "&include_rts=false&lang=en%3Fcount%3D200&include_entities=false&exclude_replies=true")

		ts = TwitterSearch(
			consumer_key = data["consumer_key"],
			consumer_secret = data["consumer_secret"],
			access_token = data["access_token"],
			access_token_secret = data["access_secret"]
		)

		def my_callback_closure(current_ts_instance): # Accepts an instance of TwitterSearch
			queries, tweets_seen = current_ts_instance.get_statistics()
			if queries > 0 and (queries % 5) == 0: # Trigger delay every 5th query
				return tweetList

		for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
			print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
			tweetList.append(tweet)

	except TwitterSearchException as e: 
		print(e)

	return tweetList


# Connects to the Twitter Python Wrapper API
def connect():
    return Twitter(auth=OAuth(access_token, access_secret, consumer_key, consumer_secret))


def main(): 
	api = connect()
	tweetList = getTweetList() 

	# Get a random one from the tweetList
	rand = randint(0,len(tweetList)-1)
	print('@%s tweeted: %s' % ( tweetList[rand]['user']['screen_name'], tweetList[rand]['text'] ))
	api.statuses.update(status='%s (Src: @%s)' % (tweetList[rand]['text'], tweetList[rand]['user']['screen_name'] ))

# Call this every hour
main()


