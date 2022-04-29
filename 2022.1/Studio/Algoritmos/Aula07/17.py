def main():
    in_range,out_range=0,0
    for i in range(1,11):
        n = int(input(f"Digite o valor {i}: "))
        in_range,out_range = value_processing(n,in_range,out_range)
    print(f"{in_range} estão entre 10 e 20.")
    print(f"{out_range} não estão entre 10 e 20.")

def value_processing(n,in_range=0,out_range=0):
    if 10<=n<=20:
        in_range+=1
    else:
        out_range+=1
    return in_range,out_range

main()