from writer import TweetWriter
import csv
from dictunicodewriter import DictUnicodeWriter
from os.path import isfile
from os.path import exists
from dicttweetformatter import DictTweetFormatter
from pprint import pprint

class CSVTweetWriter(TweetWriter):

    def __init__(self, tweets, outfile, fields = []):
        super(CSVTweetWriter, self).__init__(tweets, outfile, fields)

    def write(self):
        write_header = False
        if not exists(self.outfile):
            write_header = True
        with open(self.outfile, 'ab') as csv_file:

            writer = DictUnicodeWriter(csv_file, fieldnames=self.fields, quoting=csv.QUOTE_MINIMAL)
            if write_header:
                print "write header"
                writer.writeheader()
            #writer.writeheader()
            for tweet in self.tweets:
                tweet_dict = DictTweetFormatter(tweet, self.fields).format()
                writer.writerow(tweet_dict)

