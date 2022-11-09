from model.Pessoa import Pessoa


class Professor(Pessoa):
    
    def __init__(self, nome="", titulacao_maxima=""):
        super().__init__(nome)
        self.__titulacao_maxima=titulacao_maxima
    
    def setTitulação(self, titulacao_maxima):
        self.__titulacao_maxima=titulacao_maxima

    def getTitulação(self):
        return self.__titulacao_maxima