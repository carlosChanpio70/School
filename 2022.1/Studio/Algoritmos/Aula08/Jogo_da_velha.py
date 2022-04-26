from pdb import line_prefix


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

def Table_render(line1=[0,0,0,0,0,0],line2=[0,0,0,0,0,0],line3=[0,0,0,0,0,0]):
    line1 = Table_render_02(line1)
    line2 = Table_render_02(line2)
    line3 = Table_render_02(line3)
    return f"{line1}\n{line2}\n{line3}"

def Table_render_02(line):
    x1,x2,x3,o1,o2,o3 = line
    collum_1 = XO_Table_Render_selection(x1,o1)
    collum_2 = XO_Table_Render_selection(x2,o2)
    collum_3 = XO_Table_Render_selection(x3,o3)
    result  = f"{collum_1[0]}|{collum_2[0]}|{collum_3[0]}\n"
    result += f"{collum_1[1]}|{collum_2[1]}|{collum_3[1]}\n"
    result += f"{collum_1[2]}|{collum_2[2]}|{collum_3[2]}"
    return result

def XO_Table_Render_selection(X_select=False,O_select=False):
    if X_select:
        return [" \ / ","  X  "," / \ "]
    elif O_select:
        return [" /-\ "," | | "," \-/ "]
    else:
        return ["     ","     ","     "]

line1 = [1,0,0,0,0,0]
line2 = [0,0,0,0,0,0]
line3 = [0,0,0,0,0,0]
print(Table_render(line1,line2,line3))