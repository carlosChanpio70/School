from model.Pessoa import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, cnh):
        self.cnh = cnh
        super().__init__(nome, cpf)


    def listar2(self):
        print('PF: Metodo abstrato do contrato Pessoa...')

    def setCnh(self, cnh):
        self.cnh = cnh

    def getCnh(self):
        return self.cnh

    def toString(self):
        return '*** Pessoal Fisica: Nome:' + self.getNome() + ' CPF: ' + self.getCpf() + 'CNH: ' + self.getCnh()

