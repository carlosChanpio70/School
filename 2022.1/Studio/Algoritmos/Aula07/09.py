def main():
    n1 = int(input("Insira o primeiro valor: "))
    n2 = int(input("Insira o segundo valor: "))
    print(interval_logic_01(n1,n2))

def interval_logic_01(n1,n2):
    if n2 > n1:
        return interval_logic_02(n1,n2)
    else:
        return interval_logic_02(n2,n1)

def interval_logic_02(n1,n2):
    nr = ""
    while n2 > n1:
        nr += f"{n1}, "
        n1+=1
    nr += f"{n1}"
    return f"({nr})"

main()