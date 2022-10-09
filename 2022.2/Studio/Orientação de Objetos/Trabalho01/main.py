from model.Produto import Produto
from model.Empresa import Empresa
from model.ItemNota import ItemNota
from model.Nota import Nota
from model.Participante import Participante

def main():
    prod = Produto("Cachaça")
    emp = Empresa( 1, "Velho Barreiro", "Rio Claro, interior de São Paulo", "50.119.163/0001-66" )
    item = ItemNota( 15, 1)
    part = Participante( 1, "Renato e Carlos Alexandre", "50.119.163/0001-66" )
    nota = Nota( "09/10/2022", 666, 123123123 )

    print(prod.getDescricao())
    print(emp.getCodigo())
    print(emp.getRazao_social())
    print(emp.getEndereco())
    print(emp.getCnpj())
    print(nota.getData())
    print(nota.getNumero())
    print(nota.getVl_total(item))
    print(part.getCodigo())
    print(part.getRazao_social())
    print(part.getCnpj())
    print(item.getVl_unitario())
    print(item.getQuantidade())

if __name__=="__main__":
    main()