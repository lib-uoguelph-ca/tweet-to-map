from json import loads

class TweetWriter(object):

    def __init__(self, json_tweets, outfile, fields = []):
        self.outfile =  outfile
        self.read_tweets(json_tweets)
        self.fields = fields

    def write(self):
        raise NotImplementedError

    def read_tweets(self, tweets):
        self.tweets = loads(tweets)
