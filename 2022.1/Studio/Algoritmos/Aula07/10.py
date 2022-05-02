def main():
    n_of_n = int(input("Quantos números deseja inserir? "))
    n_input(n_of_n)

def n_input(n_of_n):
    loop = 1
    while loop <= n_of_n:
        n = int(input(f"Digite o número {loop}: "))
        loop += 1
        print(f"{n}! = {fatorial(n)}")

def fatorial(x):
    nr = 1
    for i in range(1,x+1):
        nr *= i
    return nr

main()