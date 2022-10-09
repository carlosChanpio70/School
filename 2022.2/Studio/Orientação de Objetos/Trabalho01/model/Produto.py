from model import ItemNota

class Produto():

    def __init__(self, id="", codigo=0, descricao=""):
        self.__id=id
        self.__codigo=codigo
        self.__descricao=descricao

    def setCodigo(self, codigo):
        self.__codigo=codigo

    def setDescricao(self, descricao):
        self.__descricao=descricao

    def getCodigo(self):
        return self.__codigo

    def getDescricao(self):
        return self.__descricao

    