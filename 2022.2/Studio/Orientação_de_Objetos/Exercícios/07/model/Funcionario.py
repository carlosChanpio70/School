
class Funcionario():

    def __init__(self, nome="", salarioBruto=0, totalAcres=0, totalDesc=0, salarioLiquido=0):
        self.__nome = nome
        self.__salarioBruto = salarioBruto
        self.__totalAcres = totalAcres
        self.__totalDesc = totalDesc
        self.__salarioLiquido = salarioLiquido

    def setNome(self, nome):
        self.__nome = nome

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto

    def setTotalAcres(self, totalAcres):
        self.__totalAcres = totalAcres

    def setTotalDesc(self, totalDesc):
        self.__totalDesc = totalDesc

    def getNome(self):
        return self.__nome

    def getSalarioBruto(self):
        return self.__salarioBruto

    def getTotalAcres(self):
        return self.__totalAcres

    def getTotalDesc(self):
        return self.__totalDesc

    def calcSalarioLiquido(self):
        self.__salarioLiquido = ( self.getSalarioBruto() + self.getTotalAcres() ) - self.getTotalDesc()
        return self.__salarioLiquido

    def toString(self):
        print(f"Nome: {self.getNome()} | " + f"Salário Bruto: R$ {self.getSalarioBruto()} | " + f"Total de Acréscimos: R$ {self.getTotalAcres()} | " + f"Total de Descontos: R$ {self.getTotalDesc()}\n")
        print(f"O Salário Líquido é de: R$ {self.calcSalarioLiquido()}")