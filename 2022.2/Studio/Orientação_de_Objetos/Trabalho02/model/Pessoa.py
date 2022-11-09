class Pessoa():

    def __init__(self, nome="", cpf=0, dataNascimento=0, email="", endereco="", telefone=0, identidade=0):
        self.__nome = nome
        self.__cpf = cpf
        self.__dataNascimento = dataNascimento
        self.__email = email
        self.__endereco = endereco
        self.__telefone = telefone
        self.__identidade = identidade

    def setNome(self, nome):
        self.__nome = nome

    def setCPF(self, cpf):
        self.__cpf = cpf

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
    
    def setEmail(self, email):
        self.__email = email
    
    def setEndereco(self, endereco):
        self.__endereco = endereco
    
    def setTelefone(self, telefone):
        self.__telefone = telefone
    
    def setIdentidade(self, identidade):
        self.__identidade = identidade

    def getNome(self):
        return self.__nome

    def getCPF(self):
        return self.__cpf

    def getDataNascimento(self):
        return self.__dataNascimento
    
    def getEmail(self):
        return self.__email
    
    def getEndereco(self):
        return self.__endereco
    
    def getTelefone(self):
        return self.__telefone
    
    def getIdentidade(self):
        return self.__identidade