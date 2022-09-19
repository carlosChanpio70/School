def main():
    p = Pessoa()
    p.setNome("Ahoy")
    p.__nome = "A"
    print(p.getNome())

class Pessoa():

    def __init__(self, nome="", cpf=""):
        self.__nome = nome
        self.cpf = cpf

    def setNome(self, nome):
        self.__nome = nome

    def setCpf(self, cpf):
        self.cpf = cpf

    def getNome(self):
        return self.__nome
        
    def getCpf(self):
        return self.cpf

class Pessoa_Física(Pessoa):
    def __init__(self, nome, cpf, cnh=""):
        super().__init__(nome, cpf)
        self.cnh = cnh

    def setCnh(self, cnh):
        self.cnh = cnh

    def getCnh(self):
        return self.cnh  

class Dependente():
    def __init__(self, nome="", nascimento=""):
        self.nome = nome
        self.nascimento = nascimento

class Pessoa_Jurídica(Pessoa):
    def __init__(self, nome, cpf, cnpj=""):
        super().__init__(nome, cpf)
        self.cnpj = cnpj

    def setCnpj(self, cnpj):
        self.cnpj = cnpj

    def getCnpj(self):
        return self.cnpj


if __name__ == "__main__":
    main()