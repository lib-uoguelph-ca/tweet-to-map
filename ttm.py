import tweepy
import secrets
from pprint import pprint
from util import getPlaceID

auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token_key, secrets.access_token_secret)
api = tweepy.API(auth)

search_term = "Android"

place = getPlaceID(api=api, place="Canada")
query = "place:{place}".format(place=place)
if search_term:
    query += " " + search_term
tweets = api.search(q=query, count=100)

print len(tweets)
#for tweet in tweets:
#x`    pprint(tweet)
