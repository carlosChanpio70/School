code = int(input("Inserir código de unidade: "))
if 0 < code < 5:
    if 0 < code <= 2:
        if code == 1:
            Unit = "CD-ROM (700MB)"
        else:
            Unit = "DVD-ROM (4.7GB)"
    else:
        if 2 < code <= 4:
            if code == 3:
                Unit = "DVD-9 (8.54 GB)"
            else:
                Unit = "Blu-Ray (25 GB)"
    print(f"A unidade é: {Unit}")
else:
    print("Código inválido")