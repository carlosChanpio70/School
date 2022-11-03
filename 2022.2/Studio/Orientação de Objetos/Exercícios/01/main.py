from model.Turma import Turma


def main():
    A=Turma()
    A.addAluno("Ahoy")
    A.addAluno("Beta")
    print(A.listAluno())
    A.removeAluno("Ahoy")
    print(A.listAluno())



if __name__=="__main__":
    main()