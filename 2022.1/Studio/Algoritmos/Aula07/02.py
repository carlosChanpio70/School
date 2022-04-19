for loop in range(1,21):
    number = float(input(f"Digite o número {loop}: "))
    if not loop:
        smallest = number;biggest = number
    if number < smallest:
        smallest = number
    if number > biggest:
        biggest = number
print(f"O menor número digitado é {smallest} e o maior {biggest}")