from tracemalloc import stop


w_state = 1;loop = 1;medium_value = 0
while w_state:
    number_in = int(input(f"Digite o número {loop}: "))
    if number_in<0:
        w_state=0
    else:
        loop += 1
        medium_value += number_in
medium_R = medium_value/loop
print(f"Média é: {medium_R}")