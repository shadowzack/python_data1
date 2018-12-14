class Tech:

    def __init__(self, header, qustion, tags, qId, relativeTime, href):
        self.qustion = qustion
        self.tags = tags
        self.qId = qId
        self.relativeTime = relativeTime
        self.href = href
        self.header = header

    def __str__(self):
        return "########### Tech Object: header= %s, qustion= %s, tags= %s, qId= %s,relativeTime= %s,href= %s \n\n" % (self.header, self.qustion, self.tags, self.qId, self.relativeTime, self.href)
