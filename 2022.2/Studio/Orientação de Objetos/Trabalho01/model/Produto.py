class Participante():

    def __init__(self, codigo=0, descricao=""):
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