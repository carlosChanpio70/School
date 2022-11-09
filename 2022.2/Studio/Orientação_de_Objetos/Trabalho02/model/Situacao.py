class Situacao():

    def __init__(self, situacao=0, anoSemestre=0):
        self.__situacao = situacao
        self.__anoSemestre= anoSemestre
        self.__alunos=[]

    def addAluno(self, aluno):
        self.__alunos.append(aluno)

    def removeAluno(self, aluno):
        self.__alunos.remove(aluno)

    def getAlunos(self):
        return self.__alunos

    def setSituacao(self, situacao):
        self.__situacao = situacao

    def setanoSemestre(self, anoSemestre):
        self.__anoSemestre = anoSemestre

    def getSituacao(self):
        return self.__situacao
        
    def getanoSemestre(self):
        return self.__anoSemestre

    def toString(self):
        string="Alunos: "
        for i in self.__alunos:
            string += f"{i} |"
        return f"**** Situação:\n{string} Ano/Semestre: {self.getanoSemestre()} | Situação: {self.getSituacao()}"  