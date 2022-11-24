from model.file import File

class Usuario(File):

    def __init__(self, filepath="2022.2/Studio/Orientação_de_Objetos/Trabalho_Final/files/usuarios.txt"):
        super().__init__(filepath)
        self.__filepath=filepath
        self.__logado=False
        self.__id=0
        self.__nome=""
        self.__tipo=0

    def isLogado(self):
        return self.__logado

    def Login(self):
        login=input("Digite o login: ")
        senha=input("Digite a senha: ")
        with open(self.__filepath,"r") as file:
            data = list(file)
        for i in data:
            i=i.split(',')
            if login == i[3] and senha == i[4]:
                self.__logado=True
                self.__id=i[0]
                self.__nome=i[1]
                self.__tipo=i[2]
                return "Logado com sucesso"
        print("Login ou senha inválido, tente novamente.")
        return self.Login()
