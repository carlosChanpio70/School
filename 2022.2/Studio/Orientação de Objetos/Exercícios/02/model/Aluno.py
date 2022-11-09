from model.Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, tipo_matricula, nota1, nota2, aprovado):
        Pessoa.__init__(self, nome)
        self.tipo_matricula = tipo_matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.aprovado = aprovado
    

    def toString(self):
        pass

