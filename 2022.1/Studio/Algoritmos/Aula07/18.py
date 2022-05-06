from asyncore import loop


def main():
    n_of_n = int(input("Quantos números perfeitos deseja ver? "))
    perfect_n_finder_amount(n_of_n)

def perfect_n_finder_amount(x):
    loop,find_counter = 2,0
    while find_counter<x:
        n = perfect_n_finder(loop)
        loop += 1
        if n:
            print(n)
            find_counter+=1

def perfect_n_finder(x):
    str,sum,loop,loop_check = f"{x} = 1",1,2,int(x/2)
    if x%2==0:
        while loop<=loop_check:
            if x%loop==0:
                str+=f"+{loop}"
                sum+=loop
            loop+=1
    if sum==x:
        return str
    return False

main()