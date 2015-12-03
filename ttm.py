import twitter
import secrets
from pprint import pprint
from sys import exit


api = twitter.Api(
    consumer_key=unicode(secrets.consumer_key),
    consumer_secret=unicode(secrets.consumer_secret),
    access_token_key=unicode(secrets.access_token_key),
    access_token_secret=unicode(secrets.access_token_secret)
)

user = api.VerifyCredentials()

if not user:
    print "Invalid credentials"
    exit()

search_term = "Android"
latitude = 43.653226
longitude = -79.383184
radius = "50mi"

results = api.GetSearch(term=search_term, geocode=(latitude, longitude, radius), count=100)

for tweet in results:
    print "--Tweet--"
    pprint(tweet.text)
    print "--Geo--"
    pprint(tweet.geo)
    print "--Place--"
    pprint(tweet.place)
    print "--Tags--"
    for tag in tweet.hashtags:
        print "#" + tag.text
    print "\n\n"
