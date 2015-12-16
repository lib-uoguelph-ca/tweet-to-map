class ResultParser(object):
    def __init__(self, results):
        self.results = results

    def getJSON(self):
        raise NotImplementedError
