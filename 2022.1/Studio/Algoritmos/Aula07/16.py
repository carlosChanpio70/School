def main():
    sum,sum_string = get_sum(int(input("Insira o número: ")))
    print(f"A soma é {sum_string}\nSendo o resultado final: {sum}")

def get_sum(n):
    string,sum,loop="S = 1",0,0
    while n>loop:
        loop+=1
        string = f"{string} + 1/{loop}"
        sum+=1/loop
    return sum,string

main()