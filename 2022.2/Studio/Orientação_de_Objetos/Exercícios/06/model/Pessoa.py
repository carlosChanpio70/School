
class Pessoa():

    def __init__(self, genero="", peso=0.0, altura=0.0, imc=0):
        self.__genero = genero.capitalize().strip()
        self.__peso = float(peso)
        self.__altura = float(altura)
        self.__imc = float(imc)
    
    def setGenero(self, genero):
        self.__genero = genero.capitalize().strip()

    def setPeso(self, peso):
        self.__peso = float(peso)

    def setAltura(self, altura):
        self.__altura = float(altura)

    def getGenero(self):
        return self.__genero

    def getPeso(self):
        return self.__peso

    def getAltura(self):
        return self.__altura

    def calcularImc(self):
        self.__imc = self.__peso / (self.__altura**2) # Função do cálculo de IMC
        return self.__imc
