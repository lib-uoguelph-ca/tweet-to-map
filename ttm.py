import tweepy
import secrets
import json

from pprint import pprint
from places import get_place_id
from writer import CSVTweetWriter
from results import TweepyResultParser

def process_cursor_results(tweets, max_results = 1000):
    #count = tweets.items().limit
    #print "{count} results found".format(count=count)

    num_found = 0;
    for tweet in tweets.items():
        num_found += 1
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

        if(num_found >= max_results):
            break

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
results_per_page = 10 #Max 100
result_page_count = 2
output_fields = \
    ["text",
     "created_at",
     "name",
     "screen_name",
     "location",
     "geo_enabled",
     "latitude",
     "longitude",
     "place_name",
     "place_country",
     "place_bounding_1_lat",
     "place_bounding_1_long",
     "place_bounding_2_lat",
     "place_bounding_2_long",
     "place_bounding_3_lat",
     "place_bounding_3_long",
     "place_bounding_4_lat",
     "place_bounding_4_long"
     ]

query = ""
if(location_term):
    try:
        place = get_place_id(api=api, place=location_term, granularity=location_granularity)
        query += "place:{place}".format(place=place)
    except ValueError:
        print "Bad location name, ignoring."

if search_term:
    query += " " + search_term

tweets = tweepy.Cursor(api.search, q=query, count=results_per_page)
#process_cursor_results(tweets, 200)
for page in tweets.pages(result_page_count):
    print "PAGE"
    parser  = TweepyResultParser(page)
    writer = CSVTweetWriter(parser.getJSON(), "/tmp/ttm.csv", output_fields)
    writer.write()
print "DONE!!"
