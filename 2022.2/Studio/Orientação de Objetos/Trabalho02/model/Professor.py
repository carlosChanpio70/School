from model.Pessoa import Pessoa
from model.Curso import Curso

class Professor(Pessoa):

    def __init__(self, nome="", cpf=0, dataNascimento=0, email="", endereco="", telefone=0, identidade=0, matricula="", titulacao_Maxima=0):
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
        return f"**** Professor:  \n Matricula: {self.getMatricula()} \n Turmas: {self.getTurmas()} \n Cursos: {self.getCursos()} \n Titulação Máxima: {self.getTitulacao_Maxima()}"