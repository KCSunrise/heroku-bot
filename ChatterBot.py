# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "Z1ibfzsIajVIQYpGndbOj33Gg"
consumer_secret = "p5X87DFjZrpRSkPeAq1QcGWbEcJxldjVkOUZcUuDmP08t7T2aN"
access_token = "366131619-GhQ1mZc4sP5ffobkp5lZjv8pMs9AviHhzrF5wuRq"
access_token_secret = "OOkErPvCw5OhfwHXcAvBmvP8V0XaNp0up50g52ZMI0iXp"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
