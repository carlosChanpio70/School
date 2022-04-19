n1 = float(input("Digite o salário do funcionário: "))
n2 = float(input("Digite o tempo de trabalho do funcionário: "))
if n2 <= 1:
    Aumento = 1.10
if n2 > 1:
    Aumento = 1.20
nr = n1*Aumento
print(f"O salário do funcionário é: {nr:.2f}")