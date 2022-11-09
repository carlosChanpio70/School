from model.usuario import Usuario


#Shift | Bibli0Tec


def main():
    usuario=Usuario()
    usuario.setFilepath("2022.2/Studio/Orientação_de_Objetos/Trabalho_Final/files/usuarios.txt")
    usuario.readUsuarios(0)

if __name__=="__main__":
    main()