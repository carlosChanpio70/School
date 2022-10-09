from model import Nota

class Empresa():

    def __init__(self, id="", codigo=0, razao_social="", endereco="", cnpj=""):
        self.__id=id
        self.__codigo=codigo
        self.__razao_social=razao_social
        self.__endereco=endereco
        self.__cnpj=cnpj

    def setCodigo(self, codigo):
        self.__codigo=codigo

    def setRazao_social(self, razao_social):
        self.__razao_social=razao_social

    def setEndereco(self, endereco):
        self.__endereco=endereco

    def setCnpj(self, cnpj):
        self.__cnpj=cnpj

    def getCodigo(self):
        return self.__codigo

    def getRazao_social(self):
        return self.__razao_social

    def getEndereco(self):
        return self.__endereco
        
    def getCnpj(self):
        return self.__cnpj