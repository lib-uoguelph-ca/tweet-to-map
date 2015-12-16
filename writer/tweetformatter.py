class TweetFormatter(object):

    def __init__(self, tweet, fields):
        self.tweet = tweet
        self.fields = fields

    def format(self):
        raise NotImplementedError
