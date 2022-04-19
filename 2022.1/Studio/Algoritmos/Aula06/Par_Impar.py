from random import randint


play_1_wins = 0;play_2_wins = 0
AI_select = int(input("Você deseja jogar contra o computador(1 para sim, 0 para não)? "))
play_select = int(input("O primeiro jogador será par(0) ou impar(1)? ")) #Fiz eu mesmo, Carlos Alexandre Camarino Terra
if 0 <= play_select <= 1:
    loop_range = int(input("Quantas vezes deseja jogar? "))
    loop=(loop_range//2)+(loop_range%2)
    while loop_range:
        loop_range-=1
        play_1 = int(input("Primeiro jogador, escreva o seu número: "))
        if AI_select:
            play_2 = randint(1,2)
            print(f"Computador joga {play_2}")
        else:
            play_2 = int(input("Segundo jogador, escreva o seu número: "))
        sum_1_2 = play_1 + play_2

        if AI_select:
            player_message = "Computador"
        else:
            player_message = "Segundo jogador"
        win_message_1 = f"Primeiro jogador vence, com número {sum_1_2}"
        win_message_2 = f"{player_message} vence, com número {sum_1_2}"
        
        if play_select:
            if (sum_1_2 % 2):
                results = win_message_1
                play_1_wins+=1
            else:
                results = win_message_2
                play_2_wins+=1
        else:
            if (sum_1_2 % 2):
                results = win_message_2
                play_2_wins+=1
            else:
                results = win_message_1
                play_1_wins+=1
        print(results)
        if play_1_wins==loop or play_2_wins==loop:
            loop_range=0

    if AI_select:
        player_message = "Computador"
    else:
        player_message = "Jogador 2"
    print(f"Jogador 1 venceu {play_1_wins} vezes,{player_message} venceu {play_2_wins} vezes.")
else:
    print("Valor inválido")