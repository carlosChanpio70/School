def main():
    sum,sum_string = get_sum(int(input("Insira o número: ")))
    print(f"A soma é {sum_string}\nSendo o resultado final: {sum}")

def get_sum(n):
    string,sum,loop="S = 1",0,0
    while n>loop:
        loop+=1
        string = f"{string} + 1/{loop}!"
        sum+=1/fatorial(loop)
    return sum,string

def fatorial(x):
    nr = 1
    for i in range(1,x+1):
        nr *= i
    return nr

main()