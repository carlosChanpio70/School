negative = 0
for loop in range(1,11):
    number = float(input(f"Digite o número {loop}: "))
    if number < 0:
        negative+=1
print(f"Você digitou {negative} números negativos")