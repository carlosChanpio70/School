from model.Aluno import Aluno
from model.Curso import Curso
from model.Diario import Diario
from model.Disciplina import Disciplina
from model.Instituicao import Instituicao
from model.Professor import Professor
from model.Situacao import Situacao
from model.Turma import Turma
#Grupo 6

def main():
    aluno = Aluno("Nome1", "112.111.111-33", "12/11/2022", "a@a.com", "Rua dos Bobos, número 0", 911, 56522234, 900066699, 2022, 1, "Ativo")
    aluno.addDiario("Registro 1")
    curso = Curso("Descrição")
    curso.addProfessor("Marcos Miguel")
    curso.addDisciplina("Orientação à Objetos")
    diario = Diario("vv1", "vv2", "vvS", "vvT", "Não Faltou", "Turma B", "Alunos")
    disciplina = Disciplina("Turma do Marcos Miguel", "Orientação à Objetos")
    disciplina.addTurma("B")
    instituicao = Instituicao("UniAcademia")
    instituicao.addTurma("B")
    professor = Professor("Marcos Miguel", "666.666.666-69", "24/12/1945", "emaildomarcosmiguel@uniacademia.com.br", "Endereço", 190, 33344455, 9000222222, 3323)
    professor.addTurma("B")
    professor.addCurso("Engenharia de Software")
    situacao = Situacao("Banido", 2022)
    situacao.addAluno("Carlos Alexandre")
    turma = Turma("Engenharia de Software", 2022, 1, "UniAcademia", "Orientação à Objetos", "Marcos Miguel")
    turma.addDiario("Registro 1")

    print(aluno.toString())
    print(curso.toString())
    print(diario.toString())
    print(disciplina.toString())
    print(instituicao.toString())
    print(professor.toString())
    print(situacao.toString())
    print(turma.toString())

if __name__ == "__main__":
    main()
