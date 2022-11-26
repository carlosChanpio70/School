class File():

    def __init__(self, filepath=""):
        self.__filepath=filepath

    def writeFile(self,data_in=[]):
        data=f"{data_in[0]},"
        for i in data_in[1:-1]: data+=f"{i},"
        data+=f"{data_in[-1]}\n"
        with open(self.__filepath, 'r') as file:
            lines=file.readlines()
        while True:
            if len(lines) > int(data_in[0]):
                lines[data_in[0]] = data
                break
            else:
                lines.append("\n")
        with open(self.__filepath, 'w') as file:
            file.writelines(lines)

    def readFile(self,index):
        with open(self.__filepath,"r") as file:
            data = list(file)
        for i in data:
            if "\n" in i:
                i=i[:-1]
            i=i.split(",")
            if str(index) == i[0]:
                return i