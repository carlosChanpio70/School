def main():
    _,amount_rest = 1000,0
    while _<2000:
        get_rest_check_print(_,amount_rest)
        _+=1

def get_rest_check_print(n,amount):
    if (n%11==5):
        amount = n
        print(f"{amount} tem resto 5.")

main()