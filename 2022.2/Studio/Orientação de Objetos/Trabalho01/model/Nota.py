from model.ItemNota import ItemNota
class Nota():

    def __init__(self, id="", data=0, numero=0):
        self.__id=id
        self.__data=data
        self.__numero=numero

    def setData(self, data):
        self.__data=data

    def setNumero(self, numero):
        self.__numero=numero

    def getData(self):
        return self.__data

    def getNumero(self):
        return self.__numero

    def getVl_total(self, id):
        valor = 0
        
        valor = vl_unitario*quantidade