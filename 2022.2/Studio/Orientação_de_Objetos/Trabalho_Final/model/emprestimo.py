from model.file import File

class Emprestimo(File):

    def __init__(self,filepath="2022.2/Studio/Orientação_de_Objetos/Trabalho_Final/files/emprestimos.txt"):
        super().__init__(filepath)
        self.__filepath=filepath

    def read_emprestimos(self,id):
        with open(self.__filepath,"r") as file:
            data = list(file)
        for i in data:
            i=i[:-1]
            i=i.split(",")
            if str(id) == i[1]:
                return i