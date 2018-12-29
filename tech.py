import json

class Tech:

    def __init__(self, source, header, qustion, tags, qId, year, href):
        self.source = source
        self.qustion = qustion
        self.tags = tags
        self.qId = qId
        self.year = year
        self.href = href
        self.header = header

    def __str__(self):
        return "########### Tech Object:sorce=%s, header= %s, qustion= %s, tags= %s, qId= %s, year= %s,href= %s \n\n" % (self.source, self.header, self.qustion, self.tags, self.qId, self.year, self.href)
    def toJSON(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJSON()
    @staticmethod
    def serialize(object):
        return json.dumps(object, default=lambda o: o.__dict__.values()[0])

