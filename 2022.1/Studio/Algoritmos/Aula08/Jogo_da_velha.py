def main():

    linha = ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print(f"                  Jogo da Velha\n{linha}")
    
    
    player1 = int(input("Jogador 1 - Insira o seu primeiro movimento: "))
    player2 = int(input("Jogador 2 - Insira o seu primeiro movimento: "))
    print(f"{linha}\n")

    if _:
        winner = "Jogador 1"
    else:
        winner = "Jogador 2"

    line1[x1,x2,x3,o1,o2,o3]
    line2[x1,x2,x3,o1,o2,o3]
    line3[x1,x2,x3,o1,o2,o3]
    Table_render(line1,line2,line3)

    print(f"\n{linha} O Jogador {winner} ")



def Table_render_winner_check(line=[0,0,0,0,0,0,0,0,0]):
    x1,x2,x3,x4,x5,x6,x7,x8,x9 = line
    if x1==x5==x9:
        person_won=x1
        win=[x1,0,0,0,x5,0,0,0,x9]
    elif x3==x5==x7:
        person_won=x3
        win=[0,0,x3,0,x5,0,x7,0,0]
    elif x1==x4==x7:
        person_won=x1
        win=[x1,0,0,x4,0,0,x7,0,0]
    elif x2==x5==x8:
        person_won=x2
        win=[x1,0,0,0,x5,0,0,0,x9]
    elif x3==x6==x9:
        person_won=x3
        win=[x1,0,0,0,x5,0,0,0,x9]
    elif x1==x2==x3:
        person_won=x1
        win=[x1,0,0,0,x5,0,0,0,x9]
    elif x4==x5==x6:
        person_won=x4
        win=[x1,0,0,0,x5,0,0,0,x9]
    elif x7==x8==x9:
        person_won=x7
        win=[x1,0,0,0,x5,0,0,0,x9]
    else:
        return 0,Table_render(line)
    return person_won,Table_render_win_01(line,win)

def Table_render_win_01(line,win=[0,0,0,0,0,0,0,0,0]):
    line1 = Table_render_02(line[0:3],win[0:3])
    line2 = Table_render_02(line[3:6],win[3:6])
    line3 = Table_render_02(line[6:9],win[6:9])
    line = "\n-----+-----+-----\n"
    return f"{line1}{line}{line2}{line}{line3}"

def Table_render_win_02(line,win):
    n1,n2,n3,n4,n5,n6 = line,win
    collum_1 = XO_Table_Render_selection(n1)
    collum_2 = XO_Table_Render_selection(n2)
    collum_3 = XO_Table_Render_selection(n3)
    result  = f"{collum_1[0]}|{collum_2[0]}|{collum_3[0]}\n"
    result += f"{collum_1[1]}|{collum_2[1]}|{collum_3[1]}\n"
    result += f"{collum_1[2]}|{collum_2[2]}|{collum_3[2]}"
    return result

def XO_Table_render_win_render(XO_select=False,win=False):
    if win==1:
        if XO_select == 1:
            return ["\\\\\\/ "," \X\ "," /\\\\\\"]
        else:
            return ["\/-\ "," |\| "," \-/\\"]
    elif win==2:
        if XO_select == 1:
            return [" \///"," /X/ ","///\ "]
        else:
            return [" /-\/"," |/| ","/\-/ "]
    elif win==3:
        if XO_select == 1:
            return [" \|/ ","  X  "," /|\ "]
        else:
            return [" /-\ "," ||| "," \-/ "]
    elif win==4:
        if XO_select == 1:
            return [" \ / ","--X--"," / \ "]
        elif XO_select:
            return [" /-\ ","-|-|-"," \-/ "]
    else:
        return XO_Table_Render_selection(XO_select)

def XO_Table_Render_selection(XO_select=False):
    if XO_select == 1:
        return [" \ / ","  X  "," / \ "]
    elif XO_select:
        return [" /-\ "," | | "," \-/ "]
    return ["     ","     ","     "]

def Table_render(line=[0,0,0,0,0,0,0,0,0]):
    line1 = Table_render_02(line[0:3])
    line2 = Table_render_02(line[3:6])
    line3 = Table_render_02(line[6:9])
    line = "\n-----+-----+-----\n"
    return f"{line1}{line}{line2}{line}{line3}"

def Table_render_02(line):
    n1,n2,n3 = line
    collum_1 = XO_Table_Render_selection(n1)
    collum_2 = XO_Table_Render_selection(n2)
    collum_3 = XO_Table_Render_selection(n3)
    result  = f"{collum_1[0]}|{collum_2[0]}|{collum_3[0]}\n"
    result += f"{collum_1[1]}|{collum_2[1]}|{collum_3[1]}\n"
    result += f"{collum_1[2]}|{collum_2[2]}|{collum_3[2]}"
    return result



print(Table_render([1,0,0,0,0,0,0,0,2]))