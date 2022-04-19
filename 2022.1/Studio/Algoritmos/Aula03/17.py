user_select = float(input("Digite a nota do aluno: "))
if 0 <= user_select <= 10:
    if 9 <= user_select <= 10:
        concept = "A"
    else:
        if 7 <= user_select <= 8:
            concept = "B"
        else:
            if 5 <= user_select <= 6:
                concept = "C"
            else:
                if 0 <= user_select <= 5:
                    concept = "D"
    print(f"A nota é: {concept}")
else:
    print("Nota inválida")