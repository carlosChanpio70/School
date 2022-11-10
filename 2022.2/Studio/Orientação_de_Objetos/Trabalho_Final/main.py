from model.usuario import Usuario


#Shift | Bibli0Tec
#   f/LARANJA | f/LARANJA | n/BRANCO

def main():
    usuario=Usuario()
    usuario.setFilepath("2022.2/Studio/Orientação_de_Objetos/Trabalho_Final/files/usuarios.txt")
    usuario.writeUsuarios([0,"Beta",0,"Beta","123"])
    print(usuario.readUsuarios(0))
    usuario.writeUsuarios([0,"Ahoy",0,"Ahoy","321"])
    print(usuario.readUsuarios(0))

if __name__=="__main__":
    main()