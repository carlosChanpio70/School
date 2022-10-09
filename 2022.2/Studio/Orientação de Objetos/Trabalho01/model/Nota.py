class Nota():

    def __init__(self, data, numero):
        self.__data=[data]
        self.__numero=[numero]

    def addData(self, data):
        self.__data.append(data)

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
        for i in range(1,len(class_id.getQuantidade())):
            valor = class_id.getVl_unitario()[i]*class_id.getQuantidade()[i]
            valor_total+=valor
        return valor_total