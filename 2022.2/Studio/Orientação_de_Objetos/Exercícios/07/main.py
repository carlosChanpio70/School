from model.Funcionario import Funcionario
line = "============================================================"
# Desenvolvido por Renato Fernandes e Carlos Alexandre Camarino Terra

def main():
    
    inputNome = input("Insira seu nome: ")
    inputSalBruto = float(input("Insira seu salário bruto: "))
    inputAcres = float(input("Insira o total de acréscimos: "))
    inputDesc = float(input("Insira o total de descontos: "))

    #funcNome = Funcionario.setNome(inputNome)
    #funcBruto = Funcionario.setSalarioBruto(inputSalBruto)
    #funcAcres = Funcionario.setTotalAcres(inputAcres)     # Metodo Set não funciona.
    #funcDesc = Funcionario.setTotalDesc(inputDesc)
    #funcionario = Funcionario(funcNome.getNome(), funcBruto.getSalarioBruto(), funcAcres.getTotalAcres(), funcDesc.getTotalDesc())

    funcionario = Funcionario(inputNome, inputSalBruto, inputAcres, inputDesc)

    #calculoLiquido = funcionario.calcSalarioLiquido()
    print(line)
    print("\nCálculo de Salário Líquido\n")
    print(funcionario.toString())
    print(line)

if __name__=="__main__":
    main()