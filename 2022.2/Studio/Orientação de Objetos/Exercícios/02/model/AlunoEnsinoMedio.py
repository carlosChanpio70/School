from model.Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    
    def __init__(self, nome="", matricula=0, nota1=0, nota2=0):
        super().__init__(nome, matricula, nota1, nota2, 6)
        