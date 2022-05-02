def main():
    n = int(input("Digite o valor n: "))
    loop = n
    while loop:
        multiplier = multiplier_logic(loop, n)
        print(table(multiplier,n))
        loop-=1

def table(multiplier,number):
    return f"{multiplier} X {number} = {(number*multiplier)}"

def multiplier_logic(loop,n):
    return ((n+1) - loop)

main()