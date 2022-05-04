def main():
    n_of_n = int(input("Quantos números perfeitos deseja ver? "))
    perfect_n_finder_amount(n_of_n)

def perfect_n_finder_amount(x):
    loop,_ = 1,0
    while _<x:
        n = perfect_n_finder(loop)
        loop += 1
        if n:
            print(n)
            _+=1

def perfect_n_finder(x):
    str,loop,n,sum = f"{x} = 1",0,0,1
    for loop in range(2,x+1):
        if sum<=x and x%loop==0:
            str+=f"+{loop}"
            sum+=loop
        if x==sum:
            return str
    return False

main()