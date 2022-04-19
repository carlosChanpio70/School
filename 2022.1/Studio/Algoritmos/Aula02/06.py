n1 = float(input("Digite o salário bruto: "))
n2 = float(input("Digite o valor das horas extras: "))
n3 = int(input("Digite o número de horas extras: "))
nr = (n1+(n2*n3))*0.92
print(f"O salário líquido do funcionário é: {nr:.2f}")