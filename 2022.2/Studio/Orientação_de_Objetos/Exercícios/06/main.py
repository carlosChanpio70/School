from model.Pessoa import Pessoa
# Desenvolvido por Renato Fernandes, Carlos Alexandre Camarino Terra

def main():
    line = "==================================================================" # Linha separatória
    print("Cálculo de IMC\n")
    genero = input("Insira o seu genero(M ou F): ") # Input do Sexo
    peso = float(input("Insira o seu peso(Em kg, por ex: 80.5): ")) # Input do Peso
    altura = float(input("Insira a sua altura(Em metros, por ex: 1.92): ")) # Input da Altura

    pessoa = Pessoa(genero, peso, altura) # Recebe as informações do input
    imc = pessoa.calcularImc() # Realiza o Cálculo do IMC

    print(f"{line}\nGenero: {pessoa.getGenero()} | Peso: {pessoa.getPeso():.2f}kg | Altura: {pessoa.getAltura():.2f}m")
    print(f"\nIMC: {imc:.2f}") # Mostra o resultado do IMC
    print(calculo_condição(pessoa, imc))

    # Realiza o calculo da condição e mostra o resultado.
def calculo_condição(pessoa, imc):
    if pessoa.getGenero == "M":
        imcr= [20.7,26.4,27.8,31.1]
    else:
        imcr= [19.1,25.8,27.3,32.3]
    if imc < imcr[0]:
        resultado = "Abaixo do peso."
    elif imcr[0] <= imc < imcr[1]:
        resultado = "No peso normal."
    elif imcr[1] <= imc < imcr[2]:
        resultado = "Marginalmente acima do peso."
    elif imcr[2] <= imc < imcr[3]:
        resultado = "Acima do peso ideal."
    else:
        resultado = "Obeso."
    return f"\nCondição: {resultado}"


if __name__ == "__main__":
    main()