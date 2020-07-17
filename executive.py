class Executive:
    def __init__(self):
        self.name = "임원희"
        self.__coding = 90
        self.__confidence = 100

    def controlCoding(self, num):
        self.__coding += num;

    def controlConfidence(self, num):
        self.__confidence += num;

    def getCoding(self):
        return self.__coding

    def getConfidence(self):
        return self.__confidence
