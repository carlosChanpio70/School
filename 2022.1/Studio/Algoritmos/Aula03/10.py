time = float(input("Anos em que os fundos foram mantidos: "))
if time < 1:
    value = 0.55
if 1 <= time < 2:
    value = 0.65
if 2 <= time < 3:
    value = 0.75
if 3 <= time < 4:
    value = 0.85
if 4 <= time < 5:
    value = 0.90
if 5 <= time:
    value = 0.95
print(f"A taxa de juros é de: {value}")