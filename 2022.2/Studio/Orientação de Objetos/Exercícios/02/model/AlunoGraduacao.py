from model.Aluno import Aluno

class AlunoGraduacao(Aluno):

    def __init__(self, nome, tipo_matricula, nota1, nota2, aprovado):
        Aluno.__init__(nome, tipo_matricula, nota1, nota2, aprovado)

    def calcAprovacao(self):
        calculomedia = (self.nota1 + self.nota2) / 2
        if (calculomedia) >= 7:
            self.aprovado = True
        else:
            self.aprovado = False
