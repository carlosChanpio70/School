class ItemNota():

    def __init__(self, vl_unitario, quantidade):
        self.__vl_unitario=[vl_unitario]
        self.__quantidade=[quantidade]

    def addVl_unitario(self, vlunitario):
        self.__vl_unitario.append(vlunitario)

    def addQuantidade(self, quantidade):
        self.__quantidade.append(quantidade)

    def removeVl_unitario(self, vlunitario):
        self.__vl_unitario.remove(vlunitario)

    def removeQuantidade(self, quantidade):
        self.__quantidade.remove(quantidade)

    def getVl_unitario(self):
        return self.__vl_unitario

    def getQuantidade(self):
        return self.__quantidade