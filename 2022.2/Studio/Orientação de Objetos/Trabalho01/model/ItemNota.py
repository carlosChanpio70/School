class ItemNota():

    def __init__(self, id="", vl_unitario=[], quantidade=[]):
        self.__id=id
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


p=ItemNota(0)
p.addVl_unitario(100)
p.addVl_unitario(250)
print(p.getVl_unitario)