from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome="", data_nascimento="", cr=""):
        super().__init__(nome, data_nascimento)
        self.__cr=[cr]

    def setCR(self, cr):
        self.__cr.append(cr)

    def getCR(self):
        return self.__cr

    def removeCR(self, cr):
        self.__cr.remove(cr)