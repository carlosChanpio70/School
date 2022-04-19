n = int(input("Digite um número: "))
if n == 0:
    nr = "É neutro"
if n > 0:
    nr = "É positivo"
if n < 0:
    nr = "É negativo"
print(f"{nr}")