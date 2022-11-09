from model.Pessoa import Pessoa
from model.Curso import Curso

class Professor(Pessoa):

    def __init__(self, nome="", cpf=0, dataNascimento="", email="", endereco="", telefone=0, identidade=0, matricula="", titulacao_Maxima=0):
        super().__init__(nome, cpf, dataNascimento, email, endereco, telefone, identidade)
        self.__matricula = matricula
        self.__titulacao_Maxima = titulacao_Maxima
        self.__turmas = []
        self.__cursos = []

    def addTurma(self, turma):
        self.__turmas.append(turma)

    def addCurso(self, curso):
        self.__cursos.append(curso)

    def removeTurma(self, turma):
        self.__turmas.remove(turma)

    def removeCurso(self, curso):
        self.__cursos.remove(curso)

    def getTurmas(self):
        return self.__turmas

    def getCursos(self):
        return self.__cursos

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def setTitulacao_Maxima(self, titulacao_Maxima):
        self.__titulacao_Maxima = titulacao_Maxima

    def getMatricula(self):
        return self.__matricula

    def getTitulacao_Maxima(self):
        return self.__titulacao_Maxima

    def toString(self):
        string=" Turmas: ";string2=" Cursos: "
        for i in self.__turmas:
            string += f"{i} |"
        for i in self.__cursos:
            string2 += f"{i} |"
        return f"**** Professor:\nMatricula: {self.getMatricula()} |{string}{string2} | Titulação Máxima: {self.getTitulacao_Maxima()}"