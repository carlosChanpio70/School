import string
from model.Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome="", cpf=0, dataNascimento=0, email="", endereco="", telefone=0, identidade=0, matricula="", anoInicio=0, semestreInicio=0, situacao=""):
        super().__init__(nome, cpf, dataNascimento, email, endereco, telefone, identidade)
        self.__matricula = matricula
        self.__anoInicio = anoInicio
        self.__semestreInicio = semestreInicio
        self.__situacoes = [situacao]
        self.__diarios = []

    def addSituacao(self, situacao):
        self.__situacoes.append(situacao)

    def addDiario(self, diario):
        self.__diarios.append(diario)

    def removeSituacao(self, situacao):
        self.__situacoes.remove(situacao)

    def removeDiario(self, diario):
        self.__diarios.remove(diario)

    def getSituacao(self):
        return self.__situacoes

    def getDiario(self):
        return self.__diarios

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def setAno_Inicio(self, anoInicio):
        self.__anoInicio = anoInicio

    def setSemestre_Inicio(self, anoInicio):
        self.__semestreInicio = anoInicio

    def getMatricula(self):
        return self.__matricula

    def getAno_Inicio(self):
        return self.__anoInicio

    def getSemestre_Inicio(self):
        return self.__semestreInicio

    def toString(self):
        string=""
        for i in self.__diarios:
            string += self.__diarios[i]
        return f"**** Aluno: \n  Matricula: {self.getMatricula()} | \n  Diários: {string} | Ano de Inicio: {self.getAno_Inicio()} | Semestre de Início: {self.getSemestre_Inicio}"