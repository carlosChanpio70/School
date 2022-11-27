from model.file import File

class Emprestimo(File):

    def __init__(self,filepath):
        super().__init__(filepath+"emprestimos.txt")
        self.__filepath=filepath+"emprestimos.txt"

    def setFilepath(self, filepath):
        self.__filepath=filepath+"emprestimos.txt"

    def read_emprestimos(self,id):
        with open(self.__filepath,"r") as file:
            data = list(file)
        for i in data:
            i=i[:-1]
            i=i.split(",")
            if str(id) == i[1]:
                return i