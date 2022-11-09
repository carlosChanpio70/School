class Usuario():

    def __init__(self):
        self.__filepath=""

    def setFilepath(self,filepath):
        self.__filepath=filepath

    def writeUsuarios(self,list=[0,"",0,"",""]):
        with open(self.__filepath,"w") as file:
            lines=file.readline().strip

    def readUsuarios(self,id_in):
        with open(self.__filepath,"r") as file:
            pass