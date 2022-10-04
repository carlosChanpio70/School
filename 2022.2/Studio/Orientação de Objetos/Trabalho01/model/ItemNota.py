class Participante():

    def __init__(self, vlunitario=0, quantidade=0):
        self.__vlunitario=vlunitario
        self.__quantidade=quantidade

    def setVl_unitario(self, vlunitario):
        self.__vlunitario=vlunitario

    def setQuantidade(self, quantidade):
        self.__quantidade=quantidade

    def getVl_unitario(self):
        return self.__vlunitario

    def getQuantidade(self):
        return self.__quantidade