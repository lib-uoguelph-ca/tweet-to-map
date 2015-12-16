import tweepy
import secrets
import argparse
from pprint import pprint

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

cli = argparse.ArgumentParser(description="Use the twitter API to pull tweets.")
cli.add_argument('-s', '--search-term', dest="search_term", default="", help="Search term")
cli.add_argument('-l', '--location-term', dest="location_term",  default="", help="Location term: Eg. 'Canada'")
cli.add_argument('-lg', '--location-granularity', dest="location_granularity", default="", choices=['poi', 'neighborhood', 'city', 'country', 'admin'],  help="Granularity for location lookup. One of: 'poi', 'neighborhood', 'city', 'country', or 'admin'")
cli.add_argument('-rpp', '--results-per-page', type=int, dest="results_per_page", default="100", help="Number of results to return per page. Max 100." )
cli.add_argument('-rpc', '--result-page-count', type=int, dest="result_page_count", default="1", help="Number of pages of results to return.")
cli.add_argument('-o', '--output-file', dest="output_file", required=True, help="Output file location.")
options = cli.parse_args()

query = ""
if options.location_term:
    try:
        place = get_place_id(api=api, place=options.location_term, granularity=options.location_granularity)
        query += "place:{place}".format(place=place)
    except ValueError:
        print "Bad location name, ignoring."

if options.search_term:
    query += " " + options.search_term

tweets = tweepy.Cursor(api.search, q=query, count=options.results_per_page)

#For scalability, process one page at a time.
for page in tweets.pages(options.result_page_count):
    parser  = TweepyResultParser(page)
    writer = CSVTweetWriter(parser.getJSON(), options.output_file, output_fields)
    writer.write()

print "DONE!!"
