n = int(input("Digite uma nota entre 0 e 100: "))
if 0 <= n <= 100:
    if n >= 60:
        res = "Aprovado"
    if n < 60:
        res = "Reprovado"
else:
    res = "Nota inválida"
print(res)