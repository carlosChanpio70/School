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
    print(f"\n{linha} O Jogador {who_won} venceu, com a tabela\n{table}")

#Takes the current play from the player and returns the updated list
def Table_play(line,play):
    play = [int(input(f"Jogador {play}, o que jogará? ")),play]
    if play[0]==11:
        line[0]=play[1]
    elif play[0]==12:
        line[1]=play[1]
    elif play[0]==13:
        line[2]=play[1]
    elif play[0]==21:
        line[3]=play[1]
    elif play[0]==22:
        line[4]=play[1]
    elif play[0]==23:
        line[5]=play[1]
    elif play[0]==31:
        line[6]=play[1]
    elif play[0]==32:
        line[7]=play[1]
    elif play[0]==33:
        line[8]=play[1]
    else:
        print("Valor inválido, digite novamente")
        play = play[1]
        return Table_play(line,play)
    return line

#Checks if a player has won and outputs 1 or 2 if so.
#Also outputs the current string of the Table.
def Table_render_winner_check(line):
    x1,x2,x3,x4,x5,x6,x7,x8,x9 = line
    if x1==x5==x9!=0:
        x10,x0=x1,x10+2
        line[0],line[4],line[8]=x0,x0,x0
    elif x3==x5==x7!=0:
        x10,x0=x3,x3+4
        line[2],line[4],line[6]=x0,x0,x0
    elif x1==x4==x7!=0:
        x10,x0=x1,x1+6
        line[0],line[3],line[6]=x0,x0,x0
    elif x2==x5==x8!=0:
        x10,x0=x2,x2+6
        line[1],line[4],line[7]=x0,x0,x0
    elif x3==x6==x9!=0:
        x10,x0=x3,x3+6
        line[2],line[5],line[8]=x0,x0,x0
    elif x1==x2==x3!=0:
        x10,x0=x1,x1+8
        line[0],line[1],line[2]=x0,x0,x0
    elif x4==x5==x6!=0:
        x10,x0=x4,x4+8
        line[3],line[4],line[5]=x0,x0,x0
    elif x7==x8==x9!=0:
        x10,x0=x7,x7+8
        line[6],line[7],line[8]=x0,x0,x0
    else:
        x10=0
    return x10,Table_render(line)

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