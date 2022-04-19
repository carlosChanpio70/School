n1 = float(input("Digite o salário do funcionário: "))
n2 = float(input("Digite a porcentagem do aumento: "))
na = n1*n2/100
nr = na+n1
print(f"O novo salário do funcionário é: {nr:.2f}")
print(f"O aumento foi de valor: {na:.2f}")  