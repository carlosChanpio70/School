loop_state=1;loop=1

while loop_state:
    salary = int(input(f"Digite o salário do habitante {loop}: "))
    if salary<0:
        loop_state = 0;loop-=1
    else:
        offspring = int(input(f"Digite o número de filhos do habitante {loop}: "))
        if loop==1:
            lower_than_100=0;salary_biggest=salary;salary_sum=salary
            offspring_sum=offspring
        else:
            salary_sum+=salary
            offspring_sum+=offspring
            if salary > salary_biggest:
                salary_biggest = salary
        if salary < 100:
            lower_than_100 += 1 
        loop += 1

salary_medium = salary_sum/loop
offspring_medium = offspring_sum/loop
lower_than_100 = (lower_than_100/loop)*100
print(f"A média do salário é: {salary_medium:.2f}")
print(f"A média de filhos é: {offspring_medium}")
print(f"O maior salário é {salary_biggest}")
print(f"Percentual com até R$100 de salário: {lower_than_100:.2f}%")