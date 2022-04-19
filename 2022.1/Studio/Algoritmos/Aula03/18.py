n1 = float(input("Digite o valor 1: "))
n2 = float(input("Digite o valor 2: "))
if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    Sum = n1 + n2
    if Sum < 8:
        nr = (n1+n2)/2
    if Sum == 8:
        nr = n1*n2
    if Sum > 8:
        if n1>n2:
            if n2 > 0:
                nr = n1/n2
            else:
                print("Denominador zero")
        if n2>n1:
            if n1 > 0:
                nr = n2/n1
            else:
                print("Denominador zero")
    print(f"O resultado é: {nr:.2f}")
else:
    print("Valores inválidos")