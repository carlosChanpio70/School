from Professor import Professor

class Modalidade(Professor):
    def __init__(self, nome="", data_nascimento="", cr="", descrição=""):
        super().__init__(nome, data_nascimento, cr)
        self.__descrição=[descrição]

    def setDescrição(self, descrição):
        self.__descrição.append(descrição)

    def getDescrição(self):
        return self.__descrição

    def removeDescrição(self, descrição):
        self.__descrição.remove(descrição)