def main():
    played = [];losses = [];wins = []
    game_state = False
    word_in = input("Qual será a palavra usada? ").upper()
    table_print(word_in, losses, wins)
    while not game_state:
        played, losses, wins = _play(word_in, played, losses, wins)
        game_state = win_check(word_in, played, losses)
    if game_state == 1:
        print("Você venceu com a tabela:")
    else:
        print("Você perdeu com a tabela:")
    table_print(word_in, losses, wins)


def _play(word_in, played, losses, wins):
    play = input("Digite uma letra: ").upper()
    if play in played or len(play) != 1:
        print("Valor já digitado/inválido digite novamente.")
        return _play(word_in, played, losses, wins)
    elif play in word_in:
        wins.append(play)
    else:
        losses.append(play)
    played.append(play)
    table_print(word_in, losses, wins)
    return played, losses, wins


def win_check(word_in, played, losses):
    win_n = 0;word_len = len(word_in)
    for i in word_in:
        if i in played:
            win_n += 1
    if win_n == word_len:
        return 1
    elif len(losses) == 4:
        return 2
    return False


def table_print(word_in, losses, wins):
    word_r = ""
    for i in word_in:
        if i in wins:
            word_r += i
        else:
            word_r += "_"
        word_r += " "
    if len(losses) > 0:
        arm_left = " "
    else:
        arm_left = "\\"
    if len(losses) > 1:
        arm_right = " "
    else:
        arm_right = "/"
    if len(losses) > 2:
        leg_left = " "
    else:
        leg_left = "/"
    if len(losses) > 3:
        leg_right = " "
    else:
        leg_right = "\\"
    if len(losses) == 4:
        torso = " "
    else:
        torso = "|"
    table = " ____\n"
    table += " |  |\n"
    table += f" | {arm_left}0{arm_right}\n"
    table += f" |  {torso}\n"
    table += f" | {leg_left} {leg_right}  "
    table += word_r
    print(table)


main()