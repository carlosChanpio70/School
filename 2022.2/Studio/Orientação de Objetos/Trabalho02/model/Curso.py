class Curso():

    def __init__(self, descricao=""):
        self.__descricao=descricao
        self.__professores=[]
        self.__disciplinas=[]

    def addProfessor(self, professor):
        self.__professores.append(professor)

    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def removeProfessor(self, professor):
        self.__professores.remove(professor)

    def removeDisciplina(self, disciplina):
        self.__disciplinas.remove(disciplina)

    def setDescricao(self, descricao):
        self.__descricao=descricao

    def getProfessor(self):
        return self.__professores

    def getDisciplina(self):
        return self.__disciplinas

    def getDescricao(self):
        return self.__descricao

    def toString(self):
        return f"**** Curso:  \n Disciplina: {self.getDisciplina()} \n Professor: {self.getProfessor()} \n Descrição: {self.getDescricao()}"