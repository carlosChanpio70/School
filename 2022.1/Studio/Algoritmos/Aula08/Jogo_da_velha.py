#Feito por Carlos Alexandre Camarino Terra e Renato da Silva Fernandes
def main():
    loop=1;play=[0,0,0,0,0,0,0,0,0]
    linha = ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print(f"                  Jogo da Velha\n{linha}")
    print(f"   Jogue usando coordenadas para cada ponto na tabela")
    print(f"  1 2 3\n1\n2\n3")
    while loop:
        play = Table_play(play,1)
        who_won,table = Table_render_winner_check(play)
        if who_won:
            loop=0
        else:
            print(table)
            play = Table_play(play,2)
            who_won,table = Table_render_winner_check(play)
            if who_won:
                loop=0
            else:
                print(table)
    print(f"\n{linha} O Jogador {who_won} venceu, com a tabela:\n{table}")

#Takes the current play from the player and returns the updated list
def Table_play(line,play):
    play = [int(input(f"Jogador {play}, o que jogará? ")),play]
    play_list,loop = [11,12,13,21,22,23,31,32,33],0
    if play[0] in play_list:
        while loop<9:
            line=Table_play_if(play,line,play_list,loop)
            loop += 1
    else:
        return Table_play_if_invalid(play,line)
    return line

def Table_play_if(play,line,play_check,line_index):
    if play[0]==play_check[line_index]:
        if line[line_index]==0:
            line[line_index]=play[1]
        else:
            return Table_play_if_invalid(play,line)
    return line

def Table_play_if_invalid(play,line):
    print("Valor inválido, digite novamente")
    play = play[1]
    return Table_play(line,play)

#Checks if a player has won and outputs 1 or 2 if so.
#Also outputs the current string of the Table.
def Table_render_winner_check(line):
    x1,x2,x3,x4,x5,x6,x7,x8,x9 = line
    if x1==x5==x9!=0:
        x,line = Winner_check_line_change(line,x1,2,0,4,8)
    elif x3==x5==x7!=0:
        x,line = Winner_check_line_change(line,x3,4,2,4,6)
    elif x1==x4==x7!=0:
        x,line = Winner_check_line_change(line,x1,6,0,3,6)
    elif x2==x5==x8!=0:
        x,line = Winner_check_line_change(line,x2,6,1,4,7)
    elif x3==x6==x9!=0:
        x,line = Winner_check_line_change(line,x3,6,2,5,8)
    elif x1==x2==x3!=0:
        x,line = Winner_check_line_change(line,x1,8,0,1,2)
    elif x4==x5==x6!=0:
        x,line = Winner_check_line_change(line,x4,8,3,4,5)
    elif x7==x8==x9!=0:
        x,line = Winner_check_line_change(line,x7,8,6,7,8)
    else:
        x=0
    return x,Table_render(line)

def Winner_check_line_change(line,x,y,x1,x2,x3):
    x,x0=x,x+y
    line[x1],line[x2],line[x3]=x0,x0,x0
    return x,line

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
    line1 = Table_render_02(line[0:3])
    line2 = Table_render_02(line[3:6])
    line3 = Table_render_02(line[6:9])
    line = "\n-----+-----+-----\n"
    return f"{line1}{line}{line2}{line}{line3}"

def Table_render_02(line):
    n1,n2,n3 = line
    collum_1 = XO_Table_render_selection(n1)
    collum_2 = XO_Table_render_selection(n2)
    collum_3 = XO_Table_render_selection(n3)
    result  = f"{collum_1[0]}|{collum_2[0]}|{collum_3[0]}\n"
    result += f"{collum_1[1]}|{collum_2[1]}|{collum_3[1]}\n"
    result += f"{collum_1[2]}|{collum_2[2]}|{collum_3[2]}"
    return result


main()

