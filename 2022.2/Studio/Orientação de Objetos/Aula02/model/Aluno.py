from Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome="", data_nascimento="", endereço=""):
        super().__init__(nome, data_nascimento)
        self.__endereço=endereço

    def setEndereço(self, endereço):
        self.__endereço=endereço

    def setEndereço(self):
        return self.__endereço