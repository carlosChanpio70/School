from model.Pessoa import Pessoa

class PessoaJuridica(Pessoa):

    def listar2(self):
        print('PJ: Metodo abstrato do contrato Pessoa...')

    def __init__(self, nome, cpf, cnpj):
        self.cnpj = cnpj
        super().__init__(nome, cpf)

    def setCnpj(self, cnpj):
        self.cnpj = cnpj

    def getCnpj(self):
        return self.cnpj

    def toString(self):
        return '*** Pessoal Juridica: Nome:' + self.getNome() + ' CPF: ' + self.getCpf() + 'CNPJ: ' + self.getCnpj()
