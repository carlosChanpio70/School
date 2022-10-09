class Turma():
    def __init__(self, descricao=0, ano=0, semestre=0, instituicao="", disciplina="", professor=""):
        self.__descricao=descricao
        self.__ano=ano
        self.__semestre=semestre
        self.__diarios=[]
        self.__instituicao=instituicao
        self.__disciplina=disciplina
        self.__professor=professor

    def addDiario(self, diario):
        self.__diarios.append(diario)
        
    def removeDiario(self, diario):
        self.__diarios.remove(diario)
        
    def setInstituicao(self, instituicao):
        self.__instituicao = instituicao
        
    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina
        
    def setProfessor(self, professor):
        self.__professor = professor

    def getDiarios(self):
        return self.__diarios
        
    def getInstituicao(self):
        return self.__instituicao
        
    def getDisciplina(self):
        return self.__disciplina
        
    def getProfessor(self):
        return self.__professor

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def setAno(self, ano):
        self.__ano = ano

    def setSemestre(self, semestre):
        self.__semestre = semestre

    def getDescricao(self):
        return self.__descricao

    def getAno(self):
        return self.__ano

    def getSemestre(self):
        return self.__semestre

    def toString(self):
        return f"**** Turma:  \n Instituição: {self.getInstituicao()} \n Disciplina: {self.getDisciplina()} \n Professor: {self.getProfessor()} \n Ano: {self.getAno()} \n Semestre: {self.getSemestre()} \n Diário: {self.getDiarios()} \n Descrição: {self.getDescricao()}"