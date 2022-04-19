code = int(input("Inserir o código do cargo: "))
if 100 < code <= 106:
    if 100 < code <= 103:
        if code == 101:
            job = "Vendedor"
        else:
            if code == 102:
                job = "Atendente"
            else:
                job = "Auxiliar Técnico"
    else:
        if 103 < code <= 106:
            if code == 104:
                job = "Assistente"
            else:
                if code == 105:
                    job = "Coordenador de Grupo"
                else:
                    job = "Gerente"
    print(f"O cargo correspondente é: {job}")
else:
    print("Código inválido")