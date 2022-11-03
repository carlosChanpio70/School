from model.Pessoa import Pessoa


class Aluno(Pessoa):
    
    def __init__(self, nome=""):
        super().__init__(nome)

    