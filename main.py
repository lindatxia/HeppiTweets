import twitter
import os
import json
with open('config.json') as data: 
	data = json.load(data)


consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token = data["access_token"]
access_secret = data["access_secret"]

# Log in to Twitter
tweetbot.twitter_login(consumer_key, consumer_secret, access_token, access_secret)