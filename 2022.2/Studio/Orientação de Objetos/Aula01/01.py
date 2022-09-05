class Pessoa():
    def __init__(self, nome, cpf):
        self.nome=nome
        self.cpf =cpf

class Pessoa_Física(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome,cpf)
    
class Pessoa_Jurídica(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

class Contrato(Pessoa_Jurídica):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)