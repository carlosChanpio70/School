class Diario():
    
    def __init__(self, v1=0 , v2=0, vS=0, vT=0, faltas=0, turma="", aluno=""):
        self.__v1 = v1
        self.__v2 = v2
        self.__vS = vS
        self.__vT = vT
        self.__faltas = faltas
        self.__turma = turma
        self.__aluno = aluno

    def setTurma(self, turma):
        self.__turma = turma

    def setAluno(self, aluno):
        self.__aluno = aluno

    def getTurma(self):
        return self.__turma

    def getAluno(self):
        return self.__aluno

    def setv1(self, v1):
        self.__v1 = v1

    def setv2(self, v2):
        self.__v2 = v2

    def setvS(self, vS):
        self.__vS = vS

    def setvT(self, vT):
        self.__vT = vT

    def setFaltas(self, faltas):
        self.__faltas = faltas

    def getv1(self):
        return self.__v1

    def getv2(self):
        return self.__v2

    def getvS(self):
        return self.__vS

    def getvT(self):
        return self.__vT

    def getFaltas(self):
        return self.__faltas

    def toString(self):
        return f"**** Diario:\nv1/v2/vS/VT: {self.getv1()},{self.getv2()},{self.getvS()},{self.getvT()} | Faltas: {self.getFaltas()} | Turma: {self.__turma} | Aluno: {self.__aluno}"