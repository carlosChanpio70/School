n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
n4 = float(input("Número 4: "))
if n1 < n2 and n1 < n3 and n1 < n4:
    nr = n1
else:
    if n2 < n3 and n2 < n4:
        nr = n2
    else:
        if n3 < n4:
            nr = n3
        else:
            nr = n4
print(f"É menor o número: {nr}")