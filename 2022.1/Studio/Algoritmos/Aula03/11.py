time = int(input("Ano do modelo de automóvel: "))
weight = int(input("Peso do modelo de automóvel em kg: "))
if time <= 1970:
    if weight < 1200:
        registry_tax = 16.50
        class_ = 1
    else:
        if 1200 <= weight <= 1700:
            registry_tax = 25.50
            class_ = 2
        else:
            registry_tax = 46.50
            class_ = 3
else:
    if 1970 < time < 1980:
        if weight < 1200:
            registry_tax = 27.00
            class_ = 4
        else:
            if 1200 <= weight <= 1700:
                registry_tax = 30.50
                class_ = 5
            else:
                registry_tax = 52.50
                class_ = 6
    else:
        if weight < 1600:
            registry_tax = 19.50
            class_ = 7
        else:
            registry_tax = 55.50
            class_ = 8
results = (f"{registry_tax} e {class_}")
print(f"A taxa de juros e classe são: {results}")