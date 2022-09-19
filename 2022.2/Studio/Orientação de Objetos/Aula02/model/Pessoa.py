from abc import abstractmethod


class Pessoa():
    def __init__(self, nome="", data_nascimento=""):
        self.__nome=nome
        self.__data_nascimento=data_nascimento

    def setNome(self, nome):
        self.__nome=nome

    def setNascimento(self, data_nascimento):
        self.__data_nascimento=data_nascimento

    def getNome(self):
        return self.__nome

    def getNascimento(self):
        return self.__data_nascimento

    @abstractmethod
    def getmatricula():
        pass