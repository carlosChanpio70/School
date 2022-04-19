jogador1 = int(input("Jogador 1, digite sua jogada (0=Pedra / 1=Papel / 2=Tesoura): "))
jogador2 = int(input("Jogador 2, digite sua jogada (0=Pedra / 1=Papel / 2=Tesoura): "))

if jogador1 < 0 or jogador1 > 2 or jogador2 < 0 or jogador2 > 2:
    print("Jogada inválida")
else:
    if jogador1 == jogador2:
        print("Empate")
    else:
        if jogador1 == 0:
            if jogador2 == 1:
                vencedor = 2
                mensagem = "Papel ganha de Pedra"
            else:
                vencedor = 1
                mensagem = "Pedra ganha de Tesoura"
        else:
            if jogador1 == 1:
                if jogador2 == 0:
                    vencedor = 1
                    mensagem = "Papel ganha de Pedra"
                else:
                    vencedor = 2
                    mensagem = "Tesoura ganha de Papel"
            else:
                if jogador2 == 0:
                    vencedor = 2
                    mensagem = "Pedra ganha de Tesoura"
                else:
                    vencedor = 1
                    mensagem = "Tesoura ganha de Papel"

        print(f"Jogador {vencedor} venceu ({mensagem})")