negative = 0
loop_range = int(input("Quantos números deseja digitar? "))
for loop in range(1,loop_range+1):
    number = float(input(f"Digite o número {loop}: "))
    if number < 0:
        negative+=1
print(f"Você digitou {negative} números negativos")