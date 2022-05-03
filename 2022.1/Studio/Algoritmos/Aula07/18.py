def main():
    n_of_n = int(input("Quantos números perfeitos deseja ver? "))
    perfect_n_finder_amount(n_of_n)

def perfect_n_finder_amount(x):
    loop,_ = 1,0
    while _<=x:
        n = perfect_n_finder(loop)
        loop += 1
        if n:
            print(n)
            _+=1

def perfect_n_finder(x):
    str,loop,n,sum = f"{x} = 1",0,0,1
    while loop<=x/2:
        loop += 1
        if loop!=1 and x%loop==0:
            str += f"+{loop}"
            sum += loop
        else:
            n += 1
    if loop==sum:
        return str
    else:
        return False

main()