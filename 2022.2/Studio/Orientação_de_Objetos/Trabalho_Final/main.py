from model.usuario import Usuario

def main():
    usuario=Usuario()
    usuario.setFilepath("2022.2/Studio/Orientação_de_Objetos/Trabalho_Final/files/usuarios.txt")
    usuario.writeUsuarios([0,"Ahoy",0,"Ahoy","123"])

if __name__=="__main__":
    main()