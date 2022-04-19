class Escolaridade:

    def __init__(self, escolaridade):
        self.escolaridade = escolaridade

    def setescolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def getescolaridade(self):
        return self.escolaridade

class Estado:

    def __init__(self, estado):
        self.estado = estado

    def setestado(self, estado):
        self.estado = estado

    def getestado(self):
        return self.estado

class Cidade(Estado):

    def __init__(self, estado, cidade):
        Estado.__init__(self, estado)
        self.cidade = cidade

    def setcidade(self, cidade):
        self.cidade = cidade

    def getcidade(self):
        return self.cidade

class TipoEnsino:

    def __init__(self, tipoensino):
        self.tipoensino = tipoensino

    def settipoensino(self, tipoensino):
        self.tipoensino = tipoensino

    def gettipoensino(self):
        return self.tipoensino

class Pessoa(Cidade):

    def __init__(self, estado, cidade, nome):
        Cidade.__init__(self, estado, cidade)
        self.nome = nome

    def setnome(self, nome):
        self.nome = nome

    def getnome(self):
        return self.nome

class Curso(TipoEnsino):

    def __init__(self, tipoensino):
        TipoEnsino.__init__(self, tipoensino)

class Aluno(Pessoa, Curso):

    def __init__(self, estado, cidade, nome,tipoensino):
        Pessoa.__init__(self, estado, cidade, nome)
        Curso.__init__(self, tipoensino)

class Professor(Escolaridade, Pessoa, Curso):

    def __init__(self, escolaridade, estado, cidade, nome, tipoensino):
        Escolaridade.__init__(self, escolaridade)
        Pessoa.__init__(self, estado, cidade, nome)
        Curso.__init__(self, tipoensino)

class Direção(Escolaridade, Pessoa):

    def __init__(self, escolaridade, estado, cidade, nome):
        Escolaridade.__init__(self, escolaridade)
        Pessoa.__init__(self, estado, cidade, nome)

class Coordenação(Escolaridade, Pessoa, Curso):

    def __init__(self, escolaridade, estado, cidade, nome, tipoensino):
        Escolaridade.__init__(self, escolaridade)
        Pessoa.__init__(self, estado, cidade, nome)
        Curso.__init__(self, tipoensino)

aluno = Aluno("Minas Gerais","Juiz de Fora","Macedo","Ensino Médio")
professor = Professor("5","Minas Gerais","Belo Horizonte","Raphael","Ensino Médio")
diretor = Direção("5","Rio de Janeiro","Rio de Janeiro","Markus")
coordenador = Coordenação("5","São Paulo","São Paulo","Franklin","Ensino Médio")

print(f"Aluno:\nNome: {aluno.getnome()}\nPeríodo: {aluno.gettipoensino()}")
print(f"Cidade & estado de origem:\n{aluno.getcidade()} / {aluno.getestado()}")
print(f"Professor:\nNome: {professor.getnome()}\nEnsino: {professor.gettipoensino()}")
print(f"Escolaridade: {professor.getescolaridade()}")
print(f"Cidade & estado de origem:\n{professor.getcidade()} / {professor.getestado()}")
print(f"Diretor:\nNome: {diretor.getnome()}\nEscolaridade: {diretor.getescolaridade()}")
print(f"Cidade & estado de origem:\n{diretor.getcidade()} / {diretor.getestado()}")
print(f"Coordenador:\nNome: {coordenador.getnome()}\nEscolaridade: {coordenador.getescolaridade()}")
print(f"Cidade & estado de origem:\n{coordenador.getcidade()} / {coordenador.getestado()}")