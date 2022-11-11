class Usuario():

    def __init__(self):
        self.__filepath=""

    def setFilepath(self,filepath):
        self.__filepath=filepath

    def writeUsuarios(self,l=[0,"",0,"",""]):
        with open(self.__filepath, 'r') as file:
            lines=file.readlines()
        if len(lines) > int(l[0]):
            lines[l[0]] = f"{l[0]},{l[1]},{l[2]},{l[3]},{l[4]}"
        with open(self.__filepath, 'w') as file:
            file.writelines(lines)

    def readUsuarios(self,id_in):
        with open(self.__filepath,"r") as file:
            data = list(file)
        for i in data:
            i=i.split(',')
            if str(id_in) == i[0]:
                return i