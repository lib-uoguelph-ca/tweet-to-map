from writer import TweetWriter
import csv
from dictunicodewriter import DictUnicodeWriter
from os.path import isfile
from dicttweetformatter import DictTweetFormatter
from pprint import pprint

class CSVTweetWriter(TweetWriter):

    def __init__(self, tweets, outfile, fields = []):
        super(CSVTweetWriter, self).__init__(tweets, outfile, fields)

    def create_outfile(self):
        with open(self.outfile, 'wb') as csv_file:
            writer = DictUnicodeWriter(csv_file, fieldnames=self.fields, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()

    def write(self):
        if not isfile(self.outfile):
            self.create_outfile()

        with open(self.outfile, 'wb') as csv_file:
            writer = DictUnicodeWriter(csv_file, fieldnames=self.fields)
            for tweet in self.tweets:
                tweet_dict = DictTweetFormatter(tweet, self.fields).format()
                pprint(tweet_dict)
                writer.writerow(tweet_dict)


