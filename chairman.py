class Chairman:
    def __init__(self):
        self.name = "김성익"
        self.__coding = 120
        self.__confidence = 120

    def controlCoding(self, num):
        self.__coding += num;

    def controlConfidence(self, num):
        self.__confidence += num;

    def getCoding(self):
        return self.__coding

    def getConfidence(self):
        return self.__confidence
