class Funcionario:

    def __init__(self,nome,bruto,acr,des):
        self.nome = nome
        self.bruto = bruto
        self.acr = acr
        self.des = des

    def setnome(self,nome):
        self.nome = nome

    def getnome(self):
        return self.nome

    def setbruto(self,bruto):
        self.bruto = bruto

    def getbruto(self):
        return self.bruto

    def setacr1(self,acr):
        self.acr = acr

    def getacr1(self):
        return self.acr

    def setdes1(self,des):
        self.des1 = des

    def getdes1(self):
        return self.des

    def getSalárioLíquido(self):
        return self.bruto + self.acr - self.des

nome = input("Digite o nome do funcionário:\n")
bruto = int(input("Digite o salário bruto do funcionário:\n"))
acr = int(input("Escreva o primeiro acréscimo:\n"))
des = int(input("Escreva o primeiro desconto:\n"))

funcionario1 = Funcionario(nome,bruto,acr,des)

print (f"Nome =\n{funcionario1.getnome()}")
print (f"Salário bruto =\nR${funcionario1.getbruto()}")
print (f"Salário líquido =\nR${funcionario1.getSalárioLíquido()}")