from model.Aluno import Aluno
from model.Professor import Professor
from model.Disciplina import Disciplina

class Turma():

    def __init__(self, nome=""):
        self.__nome=nome
        self.__disciplina=""
        self.__aluno=[]

    def setNome(self, nome):
        self.__nome==nome

    def getNome(self):
        return self.__nome

    def setProfessor(self, nome):
        self.__professor=Professor(nome)

    def getProfessor(self):
        return self.__professor.getNome()

    def setDisciplina(self, nome):
        self.__disciplina=Disciplina(nome)

    def getDisciplina(self):
        return self.__disciplina.getNome()

    def addAluno(self, nome):
        self.__aluno.append(Aluno(nome))

    def removeAluno(self, nome):
        for i in self.__aluno:
            if i.getNome() == nome:
                self.__aluno.remove(i)
                break

    def isAluno(self, nome):
        for i in self.__aluno:
            if i.getNome() == nome:
                return True
        return False

    def listAluno(self):
        list=""
        for i in self.__aluno:
            list += f"{i.getNome()} "
        return list