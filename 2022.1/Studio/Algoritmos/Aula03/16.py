user_select = int(input("Digite o código de seleção de usuário: "))
if 0 < user_select < 4:
    n1 = float(input("Digite o número 1: "))
    n2 = float(input("Digite o número 2: "))
    if user_select == 1:
        nr = n1 + n2
    else:
        if n2 != 0:
            print("Número 2 inválido")
        else:
            if user_select == 3:
                nr = n1 / n2
            else:
                if n1 != 0:
                    nr = n1 * n2
                else:
                    print("Número 1 inválido")
    print(f"O resultado é: {nr}")
else:
    print("Código inválido")