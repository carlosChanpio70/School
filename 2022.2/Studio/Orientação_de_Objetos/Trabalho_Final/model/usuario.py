from model.file import File
from model.emprestimo import Emprestimo
from model.livro import Livro

class Usuario(File):

    def __init__(self, filepath):
        super().__init__(filepath+"usuarios.txt")
        self.__filepath2=filepath+"usuarios.txt"
        self.__filepath=filepath
        self.__logado=False
        self.__id=0
        self.__nome=""
        self.__tipo=0

    def setFilepath(self, filepath):
        self.__filepath2=filepath+"usuarios.txt"

    def isLogado(self):
        return self.__logado

    def Login(self):
        login=input("Digite o login: ")
        senha=input("Digite a senha: ")
        with open(self.__filepath2,"r") as file:
            data = list(file)
        for i in data:
            if "\n" in i:
                i=i[:-1]
            i=i.split(',')
            if login == i[3] and senha == i[4]:
                self.__logado=True
                self.__id=i[0]
                self.__nome=i[1]
                self.__tipo=i[2]
                return "Logado com sucesso"
        print("Login ou senha inválido, tente novamente.")
        return self.Login()

    def view_Emprestimos(self):
        t=["\n  Autor: ","\nData de Empréstimo:\n",("*"*81)]
        data=Emprestimo(self.__filepath).read_emprestimos(self.getId())
        livro=Livro(self.__filepath).readFile(data[2])
        text=f"{t[2]}\nLivro 1: {livro[1]}{t[0]}{livro[2]}{t[1]}{data[3]}"
        if len(data)>4:
            livro=Livro(self.__filepath).readFile(data[4])
            text+=f"\n{t[2]}\nLivro 2: {livro[1]}{t[0]}{livro[2]}{t[1]}{data[5]}"
        if len(data)==8:
            livro=Livro(self.__filepath).readFile(data[6])
            text+=f"\n{t[2]}\nLivro 3: {livro[1]}{t[0]}{livro[2]}{t[1]}{data[7]}"
        text=f"{text}\n{t[2]}"
        print(text)

    def view_Livros(self):
        t="*"*81
        data=Livro(self.__filepath).readLivros()
        text=f"{t}\nLivro {1}: {data[0][0]}\n  Autor: {data[0][1]}"
        for i in range(1,len(data)):
            text+=f"\n{t}\nLivro {i+1}: {data[i][0]}\n  Autor: {data[i][1]}"
        text+=f"\n{t}"
        print(text)

    def getNome(self):
        return self.__nome

    def getId(self):
        return self.__id

    def getTipo(self):
        return self.__tipo