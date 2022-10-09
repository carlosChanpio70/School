from time import strptime

class Nota():

    def __init__(self, data, numero, itemNota="", participante="", empresa=""):
        self.__data=[data]
        self.__numero=[numero]
        self.__itemNotas=[itemNota]
        self.__participante=participante
        self.__empresa=empresa

    def addItemNota(self, itemNota):
        self.__itemNotas.append(itemNota)

    def removeItemNota(self, itemNota):
        self.__itemNotas.remove(itemNota)

    def setParticipante(self, participante):
        self.__participante=participante

    def setEmpresa(self, empresa):
        self.__empresa=empresa

    def getItemNotas(self):
        return self.__itemNotas

    def getParticipante(self):
        return self.__participante

    def getEmpresa(self):
        return self.__empresa

    def addData(self, data):
        self.__data.append(data.strptime('%d/%m/%Y'))

    def addNumero(self, numero):
        self.__numero.append(numero)

    def removeData(self, data):
        self.__data.remove(data)

    def removeNumero(self, numero):
        self.__numero.remove(numero)

    def getData(self):
        return self.__data

    def getNumero(self):
        return self.__numero

    def getVl_total(self, class_id):
        valor_total=0
        for i in range(len(class_id.getQuantidade())):
            valor = class_id.getVl_unitario()[i]*class_id.getQuantidade()[i]
            valor_total+=valor
        return valor_total

    def toString(self, class_id):
        string = "";string2=""
        for i in range(len(self.getData())):
            string+=f" {self.getData()[i]} | {self.getNumero()[i]} |"
        for i in self.__itemNotas:
            string2+=f" {i} |"
        return f"**** Nota:{string} {self.getVl_total(class_id)} |{string2} {self.getParticipante()} | {self.getEmpresa()}"