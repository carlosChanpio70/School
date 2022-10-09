from model import Produto,Empresa,ItemNota,Nota,Participante

def main():
    prod = Produto("Cachaça")
    print(prod.getDescricao())

    emp = Empresa("01", "Velho Barreiro", "Rio Claro, interior de São Paulo", "50.119.163/0001-66")
    print(emp.getCodigo())
    print(emp.getRazao_social())
    print(emp.getEndereco())
    print(emp.getCnpj())

    nota = Nota("09/10/2022", "000666",, "123123123")
    print(nota.getData())
    print(nota.getNumero())
    print(nota.getVl_total())

    part = Participante("01", )
    print(nota.getCodigo())
    print(nota.getRazao_social())
    print(nota.getCnpj())





if __name__=="__main__":
    main()