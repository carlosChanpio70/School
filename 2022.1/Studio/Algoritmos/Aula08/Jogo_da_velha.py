#Feito por Carlos Alexandre Camarino Terra e Renato da Silva Fernandes
def main():
    loop=1
    line = [[0,0,0,0,0,0,0,0,0],
        ["-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n","   |   |   |\n----+---+---+"]]
    print(f"                  Jogo da Velha\n{line[1][0]}")
    print(f"   Jogue usando coordenadas para cada ponto na tabela")
    print(f"  1 | 2 | 3 |\n1{line[1][1]}\n2{line[1][1]}\n3{line[1][1]}")
    while loop:
        line[0] = Table_play(line[0],1)
        who_won,table = Table_render_winner_check(line[0])
        if who_won:
            loop=0
        else:
            print(table)
            line[0] = Table_play(line[0],2)
            who_won,table = Table_render_winner_check(line[0])
            if who_won:
                loop=0
            else:
                print(table)
    if who_won==3:
        print(f"Deu velha, ",end="")
    else:
        print(f"\n{line[1][0]} O Jogador {who_won} venceu, ",end="")
    print(f"com a tabela:\n{table}")

#Takes the current play from the player and returns the updated list
def Table_play(line,play):
#Index 0 = coords default, 1 = loop start, 2 = who is playing, 3 = what has been played
    play = [[11,12,13,21,22,23,31,32,33]
    ,0,play,int(input(f"Jogador {play}, o que jogará? "))]
    if play[3] in play[0]:
        while play[1]<9:
            line=Table_play_if(line,play)
            play[1] += 1
    else:
        return Table_play_if_invalid(line,play)
    return line

def Table_play_if(line,play):
    if play[3]==play[0][play[1]]:
        if line[play[1]]==0:
            line[play[1]]=play[2]
        else:
            return Table_play_if_invalid(line,play)
    return line

def Table_play_if_invalid(line,play):
    print("Valor inválido, digite novamente")
    play = play[2]
    return Table_play(line,play)

#Checks if a player has won and outputs 1 or 2 if so.
#Also outputs the current string of the Table.
def Table_render_winner_check(line):
    x1,x2,x3,x4,x5,x6,x7,x8,x9 = line
    if x1==x5==x9!=0:
        win_r,line = Winner_check_line_change(line,x1,[2,0,4,8])
    elif x3==x5==x7!=0:
        win_r,line = Winner_check_line_change(line,x3,[4,2,4,6])
    elif x1==x4==x7!=0:
        win_r,line = Winner_check_line_change(line,x1,[6,0,3,6])
    elif x2==x5==x8!=0:
        win_r,line = Winner_check_line_change(line,x2,[6,1,4,7])
    elif x3==x6==x9!=0:
        win_r,line = Winner_check_line_change(line,x3,[6,2,5,8])
    elif x1==x2==x3!=0:
        win_r,line = Winner_check_line_change(line,x1,[8,0,1,2])
    elif x4==x5==x6!=0:
        win_r,line = Winner_check_line_change(line,x4,[8,3,4,5])
    elif x7==x8==x9!=0:
        win_r,line = Winner_check_line_change(line,x7,[8,6,7,8])
    elif not 0 in line:
        win_r=3
    else:
        win_r=0
    return win_r,Table_render(line)

def Winner_check_line_change(line,win_r,x=[0,0,0,0]):
    x0=win_r+x[0]
    line[x[1]],line[x[2]],line[x[3]]=x0,x0,x0
    return win_r,line

#Contains string data for renderer 
#Including checking wich one is going to be outputted
#1-2 Normal XO,3-6 Diagonal XO,6-10 Vertical and Horizontal XO
def XO_Table_render_selection(XO_select=False):
    if 0<XO_select<=4:
        if 0<XO_select<=2:
            if XO_select == 1:
                return [" \ / ","  X  "," / \ "]
            else:
                return [" /-\ "," | | "," \-/ "]
        elif XO_select == 3:
            return ["\\\\\\/ "," \X\ "," /\\\\\\"]
        else:
            return ["\/-\ "," |\| "," \-/\\"]
    elif 4<XO_select<=8:
        if 4<XO_select<=6:
            if XO_select == 5:
                return [" \///"," /X/ ","///\ "]
            else:
                return [" /-\/"," |/| ","/\-/ "]
        elif XO_select == 7:
            return [" \|/ ","  X  "," /|\ "]
        else:
            return [" /-\ "," ||| "," \-/ "]
    elif 8<XO_select<=10:
        if XO_select == 9:
            return [" \ / ","--X--"," / \ "]
        else:
            return [" /-\ ","-|-|-"," \-/ "]
    else:
        return ["     ","     ","     "]

#Creates the final table string.
def Table_render(line):
    line = [[
        Table_render_02(line[0:3],1),
        Table_render_02(line[3:6],2),
        Table_render_02(line[6:9],3)],
        "   1  |  2  |  3  \n",
        "\n------+-----+-----\n"]
    return f"{line[1]}{line[0][0]}{line[2]}{line[0][1]}{line[2]}{line[0][2]}"

def Table_render_02(line,x):
    collum = [
        XO_Table_render_selection(line[0]),
        XO_Table_render_selection(line[1]),
        XO_Table_render_selection(line[2])]
    return f"\
 {collum[0][0]}|{collum[1][0]}|{collum[2][0]}\n\
{x}{collum[0][1]}|{collum[1][1]}|{collum[2][1]}\n\
 {collum[0][2]}|{collum[1][2]}|{collum[2][2]}"

main()