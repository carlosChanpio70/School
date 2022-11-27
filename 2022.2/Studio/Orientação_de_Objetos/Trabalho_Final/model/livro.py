from model.file import File

class Livro(File):

    def __init__(self,filepath):
        super().__init__(filepath+"livros.txt")
        self.__filepath=filepath+"livros.txt"
    
    def setFilepath(self, filepath):
        self.__filepath=filepath+"livros.txt"

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
        
