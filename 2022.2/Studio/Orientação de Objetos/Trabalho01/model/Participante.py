class Participante():

    def __init__(self, codigo=0, razao_social="", cnpj=""):
        self.__codigo=codigo
        self.__razao_social=razao_social
        self.__cnpj=cnpj
        self.__notas=[]

    def addNota(self, nota):
        self.__notas.append(nota)

    def removeNota(self, nota):
        self.__notas.append(nota)

    def getNotas(self):
        return self.__notas

    def setCodigo(self, codigo):
        self.__codigo=codigo

    def setRazao_social(self, razao_social):
        self.__razao_social=razao_social

    def setCnpj(self, cnpj):
        self.__cnpj=cnpj

    def getCodigo(self):
        return self.__codigo

    def getRazao_social(self):
        return self.__razao_social
        
    def getCnpj(self):
        return self.__cnpj

    def toString(self):
        string=""
        for i in self.__notas:
            string+=f" {i} |"
        return f"**** Participante: {self.getCodigo()} | {self.getRazao_social()} | {self.getCnpj()} |{string}"