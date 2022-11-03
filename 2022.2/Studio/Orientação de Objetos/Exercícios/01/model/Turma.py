from model.Aluno import Aluno
from model.Professor import Professor


class Turma():
    def __init__(self):
        self.__aluno=[]

    def setProfessor(self, nome):
        self.__professor.setNome(Professor(nome))

    def getProfessor(self):
        return self.__professor.getNome()

    def addAluno(self, nome):
        aluno = Aluno(nome)
        self.__aluno.append(aluno)

    def removeAluno(self, nome):
        for i in self.__aluno:
            name = i.getNome()
            if name == nome:
                self.__aluno.remove(i)
                break

    def listAluno(self):
        list=""
        for i in self.__aluno:
            list += f" {i.getNome()}"
        return list