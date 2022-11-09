from model.Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome="", matricula=0, nota1=0, nota2=0, media=0):
        super().__init__(nome)
        self.__matricula=matricula
        self.__nota1=nota1
        self.__nota2=nota2
        self.__media=media

    def setMatricula(self, matricula):
        self.__matricula=matricula

    def getMatricula(self):
        return self.__matricula

    def setNota1(self, nota):
        self.__nota1=nota

    def getNota1(self):
        return self.__nota1

    def setNota2(self, nota):
        self.__nota1=nota
    
    def getNota2(self):
        return self.__nota2

    def getAprovado(self):
        if (self.__nota1 + self.__nota2)/2 >= self.__media:
            return True
        return False