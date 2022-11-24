from model.usuario import Usuario
from model.livro import Livro
from model.emprestimo import Emprestimo

#Shift | Bibli0Tec
#   f/LARANJA | f/LARANJA | n/BRANCO

def main():
    usuario=Usuario()
    usuario.writeFile([0,"Beta",0,"Beta","123"])
    print(usuario.readFile(0))
    print(usuario.Login())

    livro=Livro()
    livro.writeFile([0, "Livro_1", "Autor_1"])
    print(livro.readFile(0))

    emprestimo=Emprestimo()
    emprestimo.writeFile([0,0,0,"11/9/2012"])
    print(emprestimo.readFile(0))

if __name__=="__main__":
    main()