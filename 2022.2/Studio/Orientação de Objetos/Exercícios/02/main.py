from model.AlunoGraduacao import AlunoGraduacao
from model.AlunoEnsinoMedio import AlunoEnsinoMedio
from model.Professor import Professor

def main():
    prof = Professor("Marcos Miguel", "Titulacao 0")
    print(prof.getNome())
    print(prof.getTitulação())

if __name__=="__main__":
    main()