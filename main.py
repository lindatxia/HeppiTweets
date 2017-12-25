from twitter import *
from TwitterSearch import *
import json
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
		tso.set_keywords(['Blessed', 'Happy', 'Surprise', 'Believe', 'Positive', 'Celebrate', 'Engaged', 'Offer', 'Holidays', 'Beautiful', 'Nature', 'Love'],or_operator = True) # let's define all words we would like to have a look for
		tso.set_language('en') 
		tso.set_include_entities(False) 
		tso.set_positive_attitude_filter()
		tso.remove_link_filter()

		ts = TwitterSearch(
			consumer_key = data["consumer_key"],
			consumer_secret = data["consumer_secret"],
			access_token = data["access_token"],
			access_token_secret = data["access_secret"]
		)

		def my_callback_closure(current_ts_instance): # accepts ONE argument: an instance of TwitterSearch
			queries, tweets_seen = current_ts_instance.get_statistics()
			if queries > 0 and (queries % 5) == 0: # trigger delay every 5th query
				return tweetList

		for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
			#print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
			tweetList.append(tweet)

	except TwitterSearchException as e: 
		print(e)

	return tweetList


# Connects to the Twitter Python Wrapper API
def connect():
    return Twitter(auth=OAuth(access_token, access_secret, consumer_key, consumer_secret),retry=True)


def main(): 
	api = connect()
	tweetList = getTweetList() 
	print(tweetList)

main()
# Call this every 5 minutes
# api.statuses.update(status=)

