class ItemNota():

    def __init__(self, vl_unitario, quantidade, produto="", nota=0):
        self.__vl_unitario=[vl_unitario]
        self.__quantidade=[quantidade]
        self.__produto=produto
        self.__nota=nota

    def setProduto(self, produto):
        self.__produto=produto

    def setNota(self, nota):
        self.__nota=nota

    def getProduto(self):
        return self.__produto

    def getNota(self):
        return self.__nota

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

    def toString(self):
        string = ""
        for i in range(len(self.getVl_unitario())):
            string+=f" {self.getVl_unitario()[i]} | {self.getQuantidade()[i]} |"
        return f"**** ItemNota:{string} {self.getProduto()} | {self.getNota()}"