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


    print(f"\n{linha} O Jogador {winner} ")


#checks if a player has won, also runs render commands
def Table_render_winner_check(line=[0,0,0,0,0,0,0,0,0]):
    x1,x2,x3,x4,x5,x6,x7,x8,x9 = line
    if x1==x5==x9!=0:
        x10,x0=x1,x10+2
        line=[x0,x2,x3,x4,x0,x6,x7,x8,x0]
    elif x3==x5==x7!=0:
        x10,x0=x3,x3+4
        line=[x1,x2,x0,x4,x0,x6,x0,x8,x9]
    elif x1==x4==x7!=0:
        x10,x0=x1,x1+6
        line=[x0,x2,x3,x0,x5,x6,x0,x8,x9]
    elif x2==x5==x8!=0:
        x10,x0=x2,x2+6
        line=[x1,x0,x3,x4,x0,x6,x7,x0,x9]
    elif x3==x6==x9!=0:
        x10,x0=x3,x3+6
        line=[x1,x2,x0,x4,x5,x0,x7,x8,x0]
    elif x1==x2==x3!=0:
        x10,x0=x1,x1+8
        line=[x0,x0,x0,x4,x5,x6,x7,x8,x9]
    elif x4==x5==x6!=0:
        x10,x0=x4,x4+8
        line=[x1,x2,x3,x0,x0,x0,x7,x8,x9]
    elif x7==x8==x9!=0:
        x10,x0=x7,x7+8
        line=[x1,x2,x3,x4,x5,x6,x0,x0,x0]
    else:
        x10=0
    return x10,Table_render(line)

#Contains all data for the renderers
def XO_Table_render_selection(XO_select=False):
    if XO_select == 1:
        return [" \ / ","  X  "," / \ "]
    elif XO_select == 2:
        return [" /-\ "," | | "," \-/ "]
    elif XO_select == 3:
        return ["\\\\\\/ "," \X\ "," /\\\\\\"]
    elif XO_select == 4:
        return ["\/-\ "," |\| "," \-/\\"]
    elif XO_select == 5:
        return [" \///"," /X/ ","///\ "]
    elif XO_select == 6:
        return [" /-\/"," |/| ","/\-/ "]
    elif XO_select == 7:
        return [" \|/ ","  X  "," /|\ "]
    elif XO_select == 8:
        return [" /-\ "," ||| "," \-/ "]
    elif XO_select == 9:
        return [" \ / ","--X--"," / \ "]
    elif XO_select == 10:
        return [" /-\ ","-|-|-"," \-/ "]
    else:
        return ["     ","     ","     "]

#Render's the table
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

_,console = Table_render_winner_check([0,0,0,0,0,0,0,0,0])
print(_)
print(console)