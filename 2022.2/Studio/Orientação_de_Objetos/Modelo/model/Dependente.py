from model.PessoaFisica import PessoaFisica
from datetime import date, datetime, time


class Dependente:

    def getDataNascimento(self):
        return self.__dataNascimento

    def getNome(self):
        return self.__nome

    def getPessoa(self):
       return self.__pessoa

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def setNome(self, nome):
        self.__nome = nome

    def setPessoa(self, p: PessoaFisica):
        self.__pessoa = p

    def listar(self):
        data_atual = date.today()
        print (data_atual.strftime('Data: %d/%m/%Y'))

        data_hora_atual = datetime.now()
        print(data_hora_atual.strftime('Data/Hora: %d/%m/%Y %H:%M'))

        return '**** Filho:' + self.getNome() + datetime.strftime(self.getDataNascimento(), '%d-%m-%Y') + self.getPessoa().getNome()

    def toString(self):
        return '**** Dependente:' + self.getNome() + datetime.strftime(self.getDataNascimento(), '%d-%m-%Y') + self.getPessoa().getNome()
