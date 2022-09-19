from Aluno import Aluno

class Mensalidade(Aluno):
    def __init__(self, nome="", data_nascimento="", endereço="", data="", valor="[]"):
        super().__init__(nome, data_nascimento, endereço)
        self.__data=[data]
        self.__valor=[valor]

    def setData(self, data):
        self.__data.append(data)

    def setValor(self, valor):
        self.__valor.append(valor)

    def getData(self):
        return self.__data

    def getValor(self):
        return self.__valor

    def removeData(self, data):
        self.__data.remove(data)

    def removeValor(self, valor):
        self.__valor.remove(valor)