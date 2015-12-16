from tweetformatter import TweetFormatter
import types

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
            value = self.tweet[field]
            value = self._stringify(value)
            return value
        else:
            value = getattr(self, field)()
            value = self._stringify(value)
            return value

    def name(self):
        return self.tweet["user"]["name"]

    def screen_name(self):
        return self.tweet["user"]["screen_name"]

    def location(self):
        return self.tweet["user"]["location"]

    def geo_enabled(self):
        return self.tweet["user"]["geo_enabled"]

    def longitude(self):
        if "geo" not in self.tweet:
            return ""

        geo = self.tweet["geo"]

        if not geo:
            return ""

        return geo["coordinates"][0]

    def latitude(self):
        if "geo" not in self.tweet:
            return ""

        geo = self.tweet["geo"]

        if not geo:
            return ""

        return geo["coordinates"][1]

    def _encode(self, value):
        print value
        decoded = value.decode('utf8')
        print decoded
        return decoded.encode('ascii', errors='backslashreplace')

    def _stringify(self, value):
        if type(value) == types.BooleanType:
            value = str(value)

        if type(value) == types.FloatType:
            value = str(value)

        return value