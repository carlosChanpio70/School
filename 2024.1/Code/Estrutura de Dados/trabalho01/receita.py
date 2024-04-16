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

def translate_receita(receita):
    ingredientes = ""
    for i in range(len(receita[1])):
        ingredientes=+receita[1][i]+"."
    return receita[0]+","+ingredientes+","+receita[2]+","+receita[3]

def gravar_receita(receita):
    decoded=0
    file=open(os.path.join(os.path.dirname(__file__),'receitas.txt'),'r')
    for line in file:
        decoded=file.readline()
        decoded
    file=open(os.path.join(os.path.dirname(__file__),'receitas.txt'),'a')
    file.write(receita)
    pass


def listar_receitas():
    pass


def print_receita():
    pass


def main():
    pass
