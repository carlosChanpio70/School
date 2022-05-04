def main():
    n_of_n = int(input("Quantos números perfeitos deseja ver? "))
    perfect_n_finder_amount(n_of_n)

def perfect_n_finder_amount(x):
    loop,find_counter = 1,0
    while find_counter<x:
        n = perfect_n_finder(loop)
        loop += 1
        if n:
            print(n)
            find_counter+=1

def perfect_n_finder(x):
    str,sum = f"{x} = 1",1
    if x%2==0:
        for loop in range(2,int(x/2)+1):
            if x%loop==0:
                str+=f"+{loop}"
                sum+=loop
            if sum==x:
                return str
            if sum>x:
                return False
    else:
        return False

main()