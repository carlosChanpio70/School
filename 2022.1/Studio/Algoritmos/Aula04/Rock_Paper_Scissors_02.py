from random import *

jogo = int(input("Deseja jogar contra o computador (opcao = 0) ou contra um ser humano (opcao = 1)? "))
if jogo < 0 or jogo > 1:
    print("Jogo inválido")
else:
    jogador1 = int(input("Jogador 1, digite sua jogada (0=Pedra / 1=Papel / 2=Tesoura): "))
    if jogo == 0:
        jogador2 = randint(0, 2)
    else:
        jogador2 = int(input("Jogador 2, digite sua jogada (0=Pedra / 1=Papel / 2=Tesoura): "))

    if jogador1 < 0 or jogador1 > 2 or jogador2 < 0 or jogador2 > 2:
        print("Jogada inválida")
    else:
        if jogador1 == jogador2:
            print("Empate")
        else:
            if jogador1 == 0 and jogador2 == 1:
                print("Jogador 2 venceu (Papel ganha de Pedra)")
            else:
                if jogador1 == 0 and jogador2 == 2:
                    print("Jogador 1 venceu (Pedra ganha de Tesoura)")
                else:
                    if jogador1 == 1 and jogador2 == 0:
                        print("Jogador 1 venceu (Papel ganha de Pedra)")
                    else:
                        if jogador1 == 1 and jogador2 == 2:
                            print("Jogador 2 venceu (Tesoura ganha de Papel)")
                        else:
                            if jogador1 == 2 and jogador2 == 0:
                                print("Jogador 2 venceu (Pedra ganha de Tesoura)")
                            else:
                                if jogador1 == 2 and jogador2 == 1:
                                    print("Jogador 1 venceu (Tesoura ganha de Papel)")