import tweepy
import secrets
from pprint import pprint
from util import getPlaceID

auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token_key, secrets.access_token_secret)
api = tweepy.API(auth)

search_term = "BecauseIts2015"
location_term = None

query = ""
if(location_term):
    place = getPlaceID(api=api, place=location_term)
    if(place):
        query += "place:{place}".format(place=place)

if search_term:
    query += " " + search_term

tweets = api.search(q=query, count=100)

count = len(tweets)
print "{count} Results found".format(count=count)

for tweet in tweets:
    #pprint(tweet)
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

