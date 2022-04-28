def main():
    interval = input_loop()
    print(f"Há {interval[0]} números pares e {interval[1]} números impares.")
    print(f"A média de pares é: {interval[2]}")
    print(f"A média dos números é: {interval[3]}")

def input_loop():
    values=[]
    loop=1
    while loop:
        value = int(input(f"Insira o valor {loop}: "))
        if value!=0:
            values.append(value)
            loop+=1
        else:
            loop=0
    return interval_check(values)

def interval_check(values):
    even,odd,sum,amount=0,0,0,0
    for i in values:
        if not i % 2:
            even+=1
        else:
            odd+=1
    for i in values:
        sum+=i
    for i in values:
        amount+=1
    medium=get_medium(sum,amount)
    even_medium=get_medium(even,amount)
    return [even,odd,even_medium,medium]

def get_medium(n1,n2):
    return n1/n2

main()