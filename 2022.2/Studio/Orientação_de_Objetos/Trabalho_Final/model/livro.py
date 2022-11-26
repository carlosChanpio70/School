from model.file import File

class Livro(File):

    def __init__(self,filepath="2022.2/Studio/Orientação_de_Objetos/Trabalho_Final/files/livros.txt"):
        super().__init__(filepath)
        self.__filepath=filepath

    def readLivros(self):
        with open(self.__filepath,"r") as file:
            data = list(file)
        livros=[]
        for i in data:
            if "\n" in i:
                i=i[:-1]
            i=i.split(",")
            livros.append(i[1:])
        return livros
        
