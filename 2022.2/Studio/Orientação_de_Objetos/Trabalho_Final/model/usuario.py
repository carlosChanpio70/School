class Usuario():

    def __init__(self):
        self.__filepath=""

    def setFilepath(self,filepath):
        self.__filepath=filepath

    def writeUsuarios(self,list=[0,"",0,"",""]):
        usuarios=open(self.__filepath,"w")
        usuarios.write(f"{list[0]},{list[1]},{list[2]},{list[3]},{list[4]}\n")
        usuarios.close()

    def readUsuarios(self,id):
        usuarios=open(self.__filepath,"r")