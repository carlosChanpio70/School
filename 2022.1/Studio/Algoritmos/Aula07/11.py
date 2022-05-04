def main():
    n = int(input("Quantos valores deseja inserir? "))
    medium,negatives,positives = input_loop(n)
    print(f"Média é: {medium}")
    print(f"Número e porcentagem de negativos é: ",end="")
    print(f"{negatives[0]}, {negatives[1]}%")
    print(f"Número e porcentagem de positivos é: ",end="")
    print(f"{positives[0]}, {positives[1]}%")

def input_loop(n):
    values=[]
    loop=1
    while loop<=n:
        value = int(input(f"Insira o valor {loop}: "))
        values.append(value)
        loop+=1
    medium = get_medium(values,n)
    negatives,positives = negatives_positives(values,n)
    return medium,negatives,positives

def get_medium(values,n):
    value=0
    for i in values:
        value+=i
    return value/n

def negatives_positives(values,n):
    negatives,positives=0,0
    for i in values:
        if i < 0:
            negatives+=1
        elif i > 0:
            positives+=1
    negatives = [negatives,(negatives/n)*100]
    positives = [positives,(positives/n)*100]
    return negatives,positives

main()