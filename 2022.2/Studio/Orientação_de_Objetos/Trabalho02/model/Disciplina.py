class Disciplina():

    def __init__(self, descricao="", curso=""):
        self.__descricao=descricao
        self.__curso = curso
        self.__turmas = []

    def setCurso(self, curso):
        self.__curso = curso

    def addTurma(self, turma):
        self.__turmas.append(turma)

    def removeTurma(self, turma):
        self.__turmas.remove(turma)

    def getCurso(self):
        return self.__curso

    def getTurmas(self):
        return self.__turmas

    def setDescricao(self, descricao):
        self.__descricao=descricao

    def getDescricao(self):
        return self.__descricao

    def toString(self):
        string=" Turma: "
        for i in self.__turmas:
            string += f"{i} |"
        return f"**** Disciplina:\nCurso: {self.getCurso()} |{string} Descrição: {self.getDescricao()}"