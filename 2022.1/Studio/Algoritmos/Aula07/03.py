factor = int(input("Digite o número de fatorial: "))
if factor > 0:
    for loop in range(factor):
        if not loop:
            factor_R = 1
        factor_R = (loop+1)*factor_R
    print(f"{factor}! = {factor_R}")
else:
    print("Valor inválido")