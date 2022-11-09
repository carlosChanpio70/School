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
        string="Turma: "
        for i in self.__turmas:
            string += f"{i} |"
        return f"**** Instituição:\n{string} Descrição: {self.getDescricao()}"