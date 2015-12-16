from writer import TweetWriter
from csv import DictWriter
from os.path import isfile
from dicttweetformatter import DictTweetFormatter
from pprint import pprint

class CSVTweetWriter(TweetWriter):

    def __init__(self, tweets, outfile, fields = []):
        super(CSVTweetWriter, self).__init__(tweets, outfile, fields)

    def create_outfile(self):
        with open(self.outfile, 'wb') as csv_file:
            writer = DictWriter(csv_file, fieldnames=self.fields)
            writer.writeheader()


    def write(self):
        if not isfile(self.outfile):
            self.create_outfile()

        with open(self.outfile, 'wb') as csv_file:
            writer = DictWriter(csv_file, fieldnames=self.fields)
            for tweet in self.tweets:
                tweet_dict = DictTweetFormatter(tweet, self.fields).format()
                pprint(tweet_dict)
                writer.writerow(tweet_dict)


