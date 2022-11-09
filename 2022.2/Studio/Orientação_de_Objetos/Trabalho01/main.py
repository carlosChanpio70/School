from model.Produto import Produto
from model.Empresa import Empresa
from model.ItemNota import ItemNota
from model.Nota import Nota
from model.Participante import Participante
#Grupo 6

def main():    
    produto = Produto( 1,"Cachaça")
    produto.addItemNota("Cachaça")
    produto2 = Produto( 2,"Maconha")
    produto2.addItemNota("Maconha")
    participante_1 = Participante( 5, "Renato", "50.119.163/0001-66" )
    participante_2 = Participante( 6, "Carlos Alexandre", "50.119.163/0001-66" )
    empresa = Empresa( 3,"Velho Barreiro", "Rio Claro, interior de São Paulo", "50.119.163/0001-66" )
    empresa2 = Empresa( 4,"Carrefour", "Juiz de Fora, interior de Minas Gerais", "50.119.163/0001-66" )
    nota = Nota( "09/10/2022", 666, "Cachaça", "Renato", "Velho Barreiro")
    nota2 = Nota( "10/10/2022", 420, "Maconha", "Carlos Alexandre", "Carrefour")
    item = ItemNota( 15, 1, "Cachaça", 666)
    item2 = ItemNota( 10, 5, "Cachaça", 420)

    print(produto.toString())
    print(produto2.toString())
    print(empresa.toString())
    print(empresa2.toString())
    print(nota.toString(item))
    print(nota2.toString(item))
    print(participante_1.toString())
    print(participante_2.toString())    
    print(item.toString())
    print(item2.toString())

if __name__=="__main__":
    main()