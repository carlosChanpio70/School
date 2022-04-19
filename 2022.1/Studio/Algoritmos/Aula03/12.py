name = input("Nome do aluno: ")
score1 = float(input("Nota em prova 1: "))
score2 = float(input("Nota em prova 2: "))
score3 = float(input("Nota em trabalho: "))
frequency = int(input("Frequência do aluno(em faltas): "))
if 0<=score1<=10 and 0<=score2<=10 and 0<=score3<=10 and 0<=frequency:
    medium = ((score1*3) + (score2*5) + (score3*2))/10
    if frequency > 15:
        if medium > 6:
            print("Aprovado")
        else:
            print("Deverá fazer prova final")
    else:
        print("Reprovado")
else:
    print("Valor inválido")