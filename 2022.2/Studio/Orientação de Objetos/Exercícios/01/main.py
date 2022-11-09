from model.Turma import Turma
from model.Curso import Curso


#Feito por Carlos Alexandre Camarino Terra, Renato da Silva Fernandes
def main():
    A=Curso()
    A.addTurma("A")
    A.addAlunoTurma("A","Ahoy")
    A.addAlunoTurma("A","Beta")
    A.addAlunoTurma("A","Alpha")
    A.setDisciplinaTurma("A","Orientação a Objetos")
    A.setNome("Engenharia de Software")
    A.setProfessorTurma("A","Marco")

    A.addTurma("B")
    A.addAlunoTurma("B","Beta")
    A.setDisciplinaTurma("B","Orientação a Objetos")
    A.setProfessorTurma("A","Marco")

    print(A.getProfessorTurma("A"))
    print(A.getNome())
    print(A.getDisciplinaTurma("A"))
    print(A.isAlunoTurma("A","Ahoy"))
    print(A.isAlunoTurma("B","Beta"))
    print(A.isAluno("Beta"))
    print(A.isTurma("A"))

    print(A.listTurma())
    print(A.listAluno())
    print(A.listAlunoTurma("A"))
    print(A.listAlunoTurma("B"))

    A.removeAluno("Alpha")
    A.removeAlunoTurma("A","Beta")
    print(A.listAlunoTurma("A"))
    print(A.listAlunoTurma("B"))
    print(A.listAluno())


if __name__=="__main__":
    main()