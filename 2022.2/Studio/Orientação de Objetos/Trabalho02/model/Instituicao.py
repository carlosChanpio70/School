class Instituicao():

    def __init__(self, descricao=""):
        self.__descricao=descricao
        self.__turmas = []

    def addTurma(self, turma):
        self.__turmas.append(turma)
    
    def removeTurma(self, turma):
        self.__turmas.remove(turma)

    def getTurma(self):
        return self.__turmas

    def setDescricao(self, descricao):
        self.__descricao=descricao

    def getDescricao(self):
        return self.__descricao

    def toString(self):
        return f"**** Instituição:  \n Turma: {self.getTurma()} \n Descrição: {self.getDescricao()}"