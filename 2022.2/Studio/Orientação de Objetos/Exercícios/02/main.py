from model.AlunoGraduacao import AlunoGraduacao
from model.AlunoEnsinoMedio import AlunoEnsinoMedio
from model.Professor import Professor

#Feito por Carlos Alexandre Camarino Terra, Renato da Silva Fernandes
def main():
    prof = Professor("Marcos Miguel", "Titulacao 0")
    print(prof.getNome())
    print(prof.getTitulação())


    aluno1=AlunoEnsinoMedio("Ahoy",250056,5,7)
    print(aluno1.getNome())
    print(aluno1.getMatricula())
    print(aluno1.getAprovado())

    aluno2=AlunoGraduacao("Beta",255074,8,2)
    print(aluno2.getNome())
    print(aluno2.getMatricula())
    print(aluno2.getAprovado())

if __name__=="__main__":
    main()