from datetime import datetime

from model.Dependente import Dependente
from model.PessoaFisica import PessoaFisica
from model.PessoaJuridica import PessoaJuridica


#https://docs.python.org/pt-br/3/tutorial/classes.html

def principal():
    p1 = PessoaFisica('Marcos', '031', '3333')
    print(p1.toString())

    pj = PessoaFisica(nome='Paulo', cpf='031', cnh='00')
    print('Pesoa Fisica', pj.toString())
    pj.setNome('marcos')
    pj.setCpf('aaaa')
    pj.nome = '1111'
    print(pj.toString())

    pj2 = PessoaFisica('Pessoa', '0421', '222')
    pj2.setNome('mm')
    pj2.setCpf('2222')

    print(pj2.toString())

    dep1 = Dependente()
    dep1.setNome('a')
    dep1.setDataNascimento(datetime.strptime('31/08/1977', '%d/%m/%Y'))
    dep1.setPessoa(p1)
    print(dep1.toString())

    dep2 = Dependente()
    dep2.setNome('b')
    dep2.setDataNascimento(datetime.strptime('31/08/1977', '%d/%m/%Y'))
    dep2.setPessoa(p1)
    print(dep2.toString())

    p1.addDependentes(dep1)
    p1.addDependentes(dep2)

    print(p1.getDependentes()[0].toString())
    print(p1.getDependentes()[1].toString())

    p4 = PessoaJuridica('', '', '')
    p4.setCpf('000')
    p4.setNome('Nome de Pessoa Juridica')
    p4.setCnpj('0433433333')
    p4.toString()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    principal()