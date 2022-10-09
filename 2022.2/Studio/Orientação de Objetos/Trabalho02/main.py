from model.Aluno import Aluno
from model.Curso import Curso
from model.Diario import Diario
from model.Disciplina import Disciplina
from model.Instituicao import Instituicao
from model.Professor import Professor
from model.Situacao import Situacao
from model.Turma import Turma

def main():
    aluno = Aluno()
    curso = Curso()
    diario = Diario()
    disciplina = Disciplina()
    instituicao = Instituicao()
    professor = Professor()
    situacao = Situacao()
    turma = Turma()
    
    print (aluno.toString())
    print (curso.toString())
    print (diario.toString())
    print (disciplina.toString())
    print (instituicao.toString())
    print (professor.toString())
    print (situacao.toString())
    print (turma.toString())

if __name__ = "__main__":
    main()