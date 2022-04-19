class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

class Professor(Pessoa):

    def __init__(self, nome, titulo):
        Pessoa.__init__(self, nome)
        self.titulo = titulo
    
    def setTitulo(self, titulo):
        self.titulo = titulo

    def getTitulo(self):
        return self.titulo

class Aluno(Pessoa):

    def __init__(self, nome, matricula):
        Pessoa.__init__(self, nome)
        self.matricula = matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

class AlunoGraduação(Aluno):

    def __init__(self, nome, matricula, nota1, nota2):
        Aluno.__init__(self, nome, matricula)
        self.nota1 = nota1
        self.nota2 = nota2

    def setNota1(self, nota1):
        self.nota1 = nota1

    def setNota2(self, nota2):
        self.nota2 = nota2

    def getMedia(self):
        return (self.nota1 + self.nota2) / 2

class AlunoEnsinoMedio(Aluno):

    def __init__(self, nome, matricula, nota1, nota2):
        Aluno.__init__(self, nome, matricula)
        self.nota1 = nota1
        self.nota2 = nota2

    def setNota1(self, nota1):
        self.nota1 = nota1

    def setNota2(self, nota2):
        self.nota2 = nota2

    def getMedia(self):
        return (self.nota1 + self.nota2)/2

professor = Professor("Marco","Doutor")

alunoGD = AlunoGraduação("Macedo",int("0902027"),int("2"),int("5"))

alunoEM = AlunoEnsinoMedio("Josue",int("0901056"),int("5"),int("7"))

print ("Professor:")
print (f"Nome:\n    {professor.getNome()}")
print (f"Matrícula:\n   {professor.getTitulo()}")
print ("\nAluno de Graduação:")
print (f"Nome:\n  {alunoGD.getNome()}")
print (f"Matrícula:\n   {alunoGD.getMatricula()}")
if alunoGD.getMedia() >= 6:
    print ("Aluno Aprovado.")
else:
    print ("Aluno não aprovado.")
print ("\nAluno do Ensino Médio:")
print (f"Nome:\n  {alunoEM.getNome()}")
print (f"Matrícula:\n   {alunoEM.getMatricula()}")
if alunoEM.getMedia() >= 6:
    print ("Aluno Aprovado.")
else:
    print ("Aluno não aprovado.")