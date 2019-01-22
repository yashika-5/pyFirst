#!/usr/bin/pyyhon2

import tweepy
import sys
topic = sys.argv[1:]
consumer_key='uy1lo6N7sCAXF95IsjtemvIXb'
consumer_sec='HDF2ZoX6oPwz226wNUgSxcXH6dAzuYhZynlOc7N8dJZqsUdmOd'

auth=tweepy.OAuthHandler(consumer_key,consumer_sec)

access_key='744779342429884417-AZkMFxEUPh6A0qQ6Fyo5vMJ8tXhPHtv'
secret_key='BG1yyTgKzdiAIVMwMhXf7ldA7ioGnXGCUZeepMjkWDbp5'

print(dir(auth))

auth.set_access_token(access_key,secret_key)

connected = tweepy.API(auth)

tweet = connected.search(topic,count=10)

print tweet

for j in tweet :
	print j.text


