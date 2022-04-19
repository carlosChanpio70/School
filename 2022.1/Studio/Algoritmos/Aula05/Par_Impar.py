from random import randint


AI_select = int(input("Você deseja jogar contra o computador(1 para sim, 0 para não)? "))
play_select = int(input("O primeiro jogador será par(0) ou impar(1)? ")) #Fiz eu mesmo, Carlos Alexandre Camarino Terra
if 0 <= play_select <= 1:
    play_1 = int(input("Primeiro jogador, escreva o seu número: "))
    if AI_select:
        play_2 = randint(1,2)
        print(f"Computador joga {play_2}")
    else:
        play_2 = int(input("Segundo jogador, escreva o seu número: "))
    sum_1_2 = play_1 + play_2
    win_message_1 = f"Primeiro jogador vence, com número {sum_1_2}"
    if AI_select:
        win_message_2 = f"Computador vence, com número {sum_1_2}"
    else:
        win_message_2 = f"Segundo jogador vence, com número {sum_1_2}"
    if play_select:
        if (sum_1_2 % 2):
            results = win_message_1
        else:
            results = win_message_2
    else:
        if (sum_1_2 % 2):
            results = win_message_2
        else:
            results = win_message_1
    print(results)
else:
    print("Valor inválido")