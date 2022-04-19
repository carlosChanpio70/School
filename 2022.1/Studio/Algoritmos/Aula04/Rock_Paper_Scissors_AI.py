from random import randint


line = "=============================="#Carlos Alexandre Camarino Terra, Renato da Silva Fernandes, Daniel Bernardes Lima
print(f"{line}\nJogo Pedra-Papel-Tesoura, use:\n\n1 - para Pedra\n2 - para Papel\n3 - para Tesoura.\n{line}")
play_1 = int(input("Jogador, o que jogará? "))
if 1 <= play_1 <= 3:
    play_2 = randint(1,3)
    print(f"Computador jogou {play_2}")
    if play_1 == play_2:
        result = "Empate"
    else:
        if play_1 == 1:
            if play_2 == 2:
                result = "Computador vence, usando papel."
            else:
                result = "Jogador 1 vence, usando pedra."
        else:
            if play_1 == 2:
                if play_2 == 3:
                    result = "Computador vence, usando tesoura."
                else:
                    result = "Jogador 1 vence, usando papel."
            else:
                if play_2 == 1:
                    result = "Computador vence, usando pedra."
                else:
                    result = "Jogador 1 vence, usando tesoura."
    print(result)
else:
    print("Valor inválido.")