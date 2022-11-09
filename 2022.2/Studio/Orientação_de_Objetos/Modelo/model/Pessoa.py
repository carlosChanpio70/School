import abc


class Pessoa(abc.ABC):

    def __init__(self, nome, cpf):
        self.__dependentes = []
        self.__nome = nome
        self.cpf = cpf

    def setNome(self, nome):
        print('Passei aqui e peguei o nome' + nome)
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf

    def setDependentes(self, d):
        self.__dependentes = d

    def addDependentes(self, d):
        self.__dependentes.append(d)

    def removeDependentes(self, d):
        self.__dependentes.remove(d)

    def getDependentes(self):
        return self.__dependentes

    @abc.abstractmethod
    def listar2(self):
        pass

    def listar(self):
        print('Nome: ' + self.getNome() + '  CPF: ' + self.getCpf())
