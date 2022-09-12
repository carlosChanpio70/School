def main():
    p = Pessoa()
    p.setNome("Ahoy")
    print(p.getNome())

class Pessoa():

    def __init__(self, nome="", cpf=""):
        self.nome = nome
        self.cpf = cpf

    def setNome(self, nome):
        self.nome = nome

    def setcpf(self, cpf):
        self.cpf = cpf

    def getNome(self):
        return self.nome    
        
    def getcpf(self):
        return self.cpf

class Pessoa_Física(Pessoa):
    def __init__(self, nome, cpf, cnh=""):
        super().__init__(nome, cpf)
        self.cnh = cnh

    def setcnh(self, cnh):
        self.cnh = cnh

    def getcnh(self):
        return self.cnh  

class Pessoa_Jurídica(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

class Contrato(Pessoa_Jurídica):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

if __name__ == "__main__":
    main()