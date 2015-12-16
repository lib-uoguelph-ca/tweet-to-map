import tweepy
import secrets

from places import get_place_id
from writer import CSVTweetWriter
from results import TweepyResultParser

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

for page in tweets.pages(result_page_count):
    parser  = TweepyResultParser(page)
    writer = CSVTweetWriter(parser.getJSON(), "/tmp/ttm.csv", output_fields)
    writer.write()
print "DONE!!"
