from random import randint
def file_path(): return "2022.1\Studio\Algoritmos\Aula11\words.txt" #Caminho do arquivo de palavras
#Feito por Carlos Alexandre Camarino Terra

def main():
    losses = [];played = [];wins = []
    game_state = False
    word_in = word_get().upper()
    table_print(word_in, losses, wins, played)
    while not game_state:
        losses, wins, played = _play(word_in, losses, wins, played)
        game_state = win_check(word_in, losses, wins)
    if game_state == 1:
        print("Você venceu com a tabela:")
    else:
        print("Você perdeu com a tabela:")
    table_print(word_in, losses, wins, played)

def word_get():
    file = open(file_path(), "r")
    words = file.readlines()
    file.close()
    return words[randint(0, len(words)-1)].strip()

def _play(word_in, losses, wins, played):
    play = input("Digite uma letra: ").upper()
    if play in losses+wins or len(play) != 1:
        print("Valor já digitado/inválido digite novamente.")
        return _play(word_in, losses, wins)
    elif play in word_in:
        wins.append(play)
    else:
        losses.append(play)
    played.append(play)
    table_print(word_in, losses, wins, played)
    return losses, wins, played

def win_check(word_in, losses, wins):
    win_n = 0
    word_len = len(word_in)
    for i in word_in:
        if i in losses+wins:
            win_n += 1
    if win_n == word_len:
        return 1
    elif len(losses) > 5:
        return 2
    return False

def table_print(word_in, losses, wins, played):
    word_r = "";played_r = ""
    for i in word_in:
        if i in wins:   word_r += i
        else:           word_r += "_"
        word_r += " "
    for i in played:    played_r += f" {i}"
    if len(losses) > 0: head = "0"
    else:               head = " "
    if len(losses) > 1: torso = "|"
    else:               torso = " "
    if len(losses) > 2: leg_left = "/"
    else:               leg_left = " "
    if len(losses) > 3: leg_right = "\\"
    else:               leg_right = " "
    if len(losses) > 4: arm_right = "/"
    else:               arm_right = " "
    if len(losses) > 5: arm_left = "\\"
    else:               arm_left = " "
    table = f"\n ____{played_r}\n |  |\n | {arm_left}{head}{arm_right}\n"
    table += f" |  {torso}\n | {leg_left} {leg_right}  {word_r}"
    print(table)

main()