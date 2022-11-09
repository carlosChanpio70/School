from model import ItemNota

class Produto():

    def __init__(self, codigo=0, descricao=""):
        self.__codigo=codigo
        self.__descricao=descricao
        self.__item_notas=[]

    def addItemNota(self, itemNota):
        self.__item_notas.append(itemNota)

    def removeItemNota(self, itemNota):
        self.__item_notas.append(itemNota)

    def getItemNotas(self):
        return self.__item_notas

    def setCodigo(self, codigo):
        self.__codigo=codigo

    def setDescricao(self, descricao):
        self.__descricao=descricao

    def getCodigo(self):
        return self.__codigo

    def getDescricao(self):
        return self.__descricao

    def toString(self):
        string=""
        for i in self.__item_notas:
            string+=f" {i} |"
        return f"**** Produto: {self.getCodigo()} | {self.getDescricao()} |{string}"
    