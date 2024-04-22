# ? receitas=open(os.path.join(os.path.dirname(__file__),'receitas.txt'),'')
# ? r=read w=write a=append r+=read and update w+=write and update a+=append and update

''' Gravar uma nova receita no formato:
Nome da receita

Ingredientes

Modo de preparo

descrição sumária do modo de preparo

 receita=[
        'Nome da receita',
        ['Ingredientes'],
        'Modo de preparo',
        'descrição sumária do modo de preparo'
    ]

'''

import os

def receita_to_string(receita):
    ingredientes = ""
    for i in range(len(receita[1])):
        ingredientes=ingredientes+receita[1][i]+"."
    return receita[0]+","+ingredientes[:-1]+","+receita[2]

def string_to_receita(string):
    receita=[]
    string=string.split(",")
    if len(string) < 3:
        return None
    receita.append(string[0])
    receita.append(string[1].split("."))
    receita.append(string[2])
    return receita

def gravar_receita(receita):
    decoded=0
    file=open(os.path.join(os.path.dirname(__file__),'receitas.txt'),'r')
    for line in file:
        decoded=string_to_receita(line)
        if decoded==None:
            file.close()
            break
        elif decoded[0]==receita[0]:
            print(f"Receita {receita[0]} ja existe")
            file.close()
            return
    file=open(os.path.join(os.path.dirname(__file__),'receitas.txt'),'a')
    file.write(f"{receita_to_string(receita)}\n")
    file.close()


def ler_receita(nome_receita):
    file=open(os.path.join(os.path.dirname(__file__),'receitas.txt'),'r')
    for line in file:
        receita = string_to_receita(line)
        if receita is not None:
            if receita[0].strip().lower() == nome_receita.strip().lower():
                file.close()
                return receita
    file.close()
    return None

def print_receita(receita):
    print("-"*20+f"\nNome da Receita:\n{receita[0]}\nIngredientes:")
    for i in range(len(receita[1])):
        print(f"{i+1}: {receita[1][i]}")
    print(f"Modo de preparo:\n{receita[2]}")

def listar_receitas():
    file=open(os.path.join(os.path.dirname(__file__),'receitas.txt'),'r')
    for line in file:
        receita = string_to_receita(line)
        if receita is not None:
            print_receita(receita)
    file.close()

def main():
    print("O que voce deseja fazer?\n\n1 - Criar receita\n2 - Consultar receita\n3 - Listar receitas\n4 - Limpar arquivo\n5 - Sair\n")
    op=int(input())
    if op==1:
        receita=[
            'Nome da receita',
            ['Ingredientes'],
            'Modo de preparo'
        ]
        print("Nome da receita:")
        receita[0]=input()
        print("Ingrediente a ser adicionado:")
        receita[1][0]=input()
        print("Deseja adicionar mais ingredientes? 1-sim 0-nao")
        op=int(input())
        if op==1:
            while op==1:
                print("Ingrediente a ser adicionado:")
                receita[1].append(input())
                print("Deseja adicionar mais ingredientes?")
                op=int(input())
                if op==0:
                    break
        print("Modo de preparo:")
        receita[2]=input()
        gravar_receita(receita)
    elif op==2:
        listar_receitas()
    elif op==3:
        print("Digite o nome da receita")
        n = input()
        n = ler_receita(n)
        if n is None:
            print("Receita inexistente")
        else:
            print_receita(n)
    elif op==4:
        file = open(os.path.join(os.path.dirname(__file__),'receitas.txt'),'w')
        file.write("")
        file.close()
    elif op==5:
        exit()
    main()

main()
