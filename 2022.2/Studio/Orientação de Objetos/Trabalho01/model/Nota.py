class Participante():

    def __init__(self, data=0, numero=0):
        self.__data=data
        self.__numero=numero

    def setData(self, data):
        self.__data=data

    def setNumero(self, numero):
        self.__numero=numero

    def getData(self):
        return self.__data

    def getNumero(self):
        return self.__numero