from results import ResultParser
import json

class TweepyResultParser(ResultParser):
    def __init__(self, results):
        super(TweepyResultParser, self).__init__(results)
        self.output = []
        self.encoder = json.JSONEncoder()

    def getJSON(self):
        for tweet in self.results:
            self.output.append(tweet._json)
        return json.dumps(self.output)


