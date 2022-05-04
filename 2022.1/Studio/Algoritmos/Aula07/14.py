def main():
    i = int(input("De quantos produtos deseja calcular o aumento? "))
    values01,values02,medium = get_prices(i)
    loop=0
    print(f"\n|Preço dado|Novo preço\n")
    while i>loop:
        print(f"|R${values01[loop]}|R${values02[loop]}")
        loop+=1
    print(f"A média dos valores dados é {medium[0]}")
    print(f"A média dos novos valores é {medium[1]}")

def get_prices(i):
    loop,values = 1,[]
    while i>=loop:
        values.append(int(input(f"Insira o preço do produto {loop}: ")))
        loop+=1
    return values_processing(values,i)

def values_processing(prod_amount,values_given=[]):
    values_new,value_sum,medium = [],0,[]
    for value in values_given:
        values_new.append((value*1.2))
        value_sum += value
    medium[0]=(value_sum/prod_amount)
    value_sum=0
    for value in values_new:
        value_sum+=value
    medium[1]=(value_sum/prod_amount)
    return values_given,values_new,medium

main()