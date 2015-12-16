from tweetformatter import TweetFormatter

class DictTweetFormatter(TweetFormatter):

    def __init__(self, tweet, fields):
        super(DictTweetFormatter, self).__init__(tweet, fields)
        self.output = {}

    def format(self):
        for field in self.fields:
            self.output[field] = self.getFieldValue(field)

        return self.output


    def getFieldValue(self, field):
        if field in self.tweet:
            return self.tweet[field]
        else:
            return getattr(self, field)()

    def _name(self):
        return self.tweet["user"]["name"]

    def _screen_name(self):
        return self.tweet["user"]["screen_name"]

    def _location(self):
        return self.tweet["user"]["location"]

    def _geo_enabled(self):
        return self.tweet["user"]["geo_enabled"]

    def _longitude(self):
        if "geo" not in self.tweet:
            return ""

        geo = self.tweet["geo"]

        if not geo:
            return ""

        return geo["coordinates"][0]

    def _latitude(self):
        if "geo" not in self.tweet:
            return ""

        geo = self.tweet["geo"]

        if not geo:
            return ""

        return geo["coordinates"][1]


