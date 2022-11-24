class File():

    def __init__(self, filepath=""):
        self.__filepath=filepath

    def writeFile(self,l=[]):
        data=f"{l[0]},"
        for i in l[1:-1]: data+=f"{i},"
        data+=f"{l[-1]}"
        with open(self.__filepath, 'r') as file:
            lines=file.readlines()
        while True:
            if len(lines) > int(l[0]):
                lines[l[0]] = data
                break
            else:
                lines.append("\n")
        with open(self.__filepath, 'w') as file:
            file.writelines(lines)

    def readFile(self,index):
        with open(self.__filepath,"r") as file:
            data = list(file)
        for i in data:
            i=i.split(",")
            if str(index) == i[0]:
                return i