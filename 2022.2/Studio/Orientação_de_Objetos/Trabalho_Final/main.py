#Desenvolvido por: Carlos Alexandre, Renato Fernandes, Pablo do Carmo Guthier, Iverson Andrade.
import sys
from model.usuario import Usuario
from model.livro import Livro
from model.emprestimo import Emprestimo
#Shift | Bibli0Tech

def main():
    filepath="2022.2/Studio/Orientação_de_Objetos/Trabalho_Final/files/"
    usuario=Usuario(filepath)
    
    inicio()
    print(usuario.Login())
    print(f"Bem vindo! {usuario.getNome()}")
    while True:
        menu(usuario)

def menu(usuario):
    if usuario.getTipo():
        command=int(input("Selecione um comando:\n1 -=- Visualizar Empréstimos\n2 -=- Visualizar Livros\n3 -=- Sobre\n4 -=- Sair\n"))
        if command==1:
            usuario.view_Emprestimos()
        elif command==2:
            usuario.view_Livros()
        elif command==3:
            print(sobre())
        elif command==4:
            sys.exit()

def inicio():
    print(f"{inicio_txt()}\n                                 Empresa Shift\n")
    print(f"{inicio_txt()}\n                         Sejam Bem-Vindos ao Bibli0Tech!\n")

def sobre():
    text=f"{inicio_txt()}\nNomes: Carlos Alexandre, Renato Fernandes, Pablo do Carmo Guthier, Iverson Andrade\n"
    text+=f"{inicio_txt()}\n                    DESENVOLVEDORES:Carlos Alexandre, Renato Fernandes \n"
    text+="                    DESIGNERS:Renato Fernandes \n                    ANALISTAS:Pablo Guthier \n"
    text+=f"                    TESTADOR UX:Iverson Andrade\n{inicio_txt()}\nSOBRE O Bibli0tech:\n"
    text+="O aplicativo Bibli0Tech foi desenvolvido pela empresa Shift com o intuito de organizar\n"
    text+="Uma biblioteca e auxiliar os usuários a identificar quais livros estão disponíveis e ver quais já foram alugados.\n"
    return text

def inicio_txt():return ("*"*81)

if __name__=="__main__":
    main()