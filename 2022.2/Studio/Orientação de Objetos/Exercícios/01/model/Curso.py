from model.Aluno import Aluno
from model.Turma import Turma


class Curso():
    
    def __init__(self, nome=""):
        self.__nome=nome
        self.__aluno=[]
        self.__turma=[]

    def setNome(self, nome):
        self.__nome=nome

    def getNome(self):
        return self.__nome

    def addAluno(self, nome):
        status=0
        for i in self.__aluno:
            if i.getNome()==nome:
                status=1
                break
        if status==0:
            self.__aluno.append(Aluno(nome))

    def removeAluno(self, nome):
        for i in self.__aluno:
            if i.getNome() == nome:
                self.__aluno.remove(i)
                break
        for i in self.__turma:
            if i.isAluno(nome):
                i.removeAluno(nome)

    def addTurma(self, nome):
        self.__turma.append(Turma(nome))

    def removeTurma(self, nome):
        for i in self.__turma:
            if i.getNome() == nome:
                self.__turma.remove(i)
                break

    def setProfessorTurma(self, turma, nome):
        for i in self.__turma:
            if i.getNome() == turma:
                i.setProfessor(nome)
                break

    def getProfessorTurma(self, turma):
        for i in self.__turma:
            if i.getNome() == turma:
                return i.getProfessor()

    def setDisciplinaTurma(self, turma, nome):
        for i in self.__turma:
            if i.getNome() == turma:
                i.setDisciplina(nome)
                break

    def getDisciplinaTurma(self, turma):
        for i in self.__turma:
            if i.getNome() == turma:
                return i.getDisciplina()

    def addAlunoTurma(self, turma, nome):
        for i in self.__turma:
            if i.getNome() == turma:
                self.addAluno(nome)
                i.addAluno(nome)
                break

    def removeAlunoTurma(self, turma, nome):
        j=0
        for i in self.__turma:
            if not i.isAluno(nome):
                j+=1
            if i.getNome() == turma:
                i.removeAluno(nome)
        if j==1:
            self.removeAluno(nome)

    def isAluno(self, nome):
        for i in self.__aluno:
            if i.getNome() == nome:
                return True
        return False

    def isTurma(self, nome):
        for i in self.__turma:
            if i.getNome() == nome:
                return True
        return False

    def isAlunoTurma(self, turma, nome):
        for i in self.__turma:
            if i.getNome() == turma:
                return i.isAluno(nome)

    def listAluno(self):
        list=""
        for i in self.__aluno:
            list += f"{i.getNome()} "
        return list

    def listAlunoTurma(self, turma):
        for i in self.__turma:
            if i.getNome() == turma:
                return i.listAluno()

    def listTurma(self):
        list=""
        for i in self.__turma:
            list += f"{i.getNome()} "
        return list
