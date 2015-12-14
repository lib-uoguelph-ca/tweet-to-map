import tweepy
import secrets
from pprint import pprint
from util import getPlaceID

def processCursorResults(tweets):
    #count = tweets.items().limit
    #print "{count} Results found".format(count=count)

    for tweet in tweets.items():
        pprint(tweet.text)
        print "Place: "
        pprint(tweet.place)
        place = tweet.place

        if(place):
            pprint(place.full_name)
            pprint(place.country)

        print "Geo: "
        pprint(tweet.geo)
        print "Coordinates"
        pprint(tweet.coordinates)

auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token_key, secrets.access_token_secret)
api = tweepy.API(
    auth,
    wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True
)

search_term = ""
location_term = "Canada"
location_granularity = "country"

query = ""
if(location_term):
    try:
        place = getPlaceID(api=api, place=location_term, granularity=location_granularity)
        query += "place:{place}".format(place=place)
    except ValueError:
        print "Bad location name, ignoring."

if search_term:
    query += " " + search_term

#tweets = api.search(q=query, count=100)

tweets = tweepy.Cursor(api.search, q=query, count=100)
processCursorResults(tweets)

