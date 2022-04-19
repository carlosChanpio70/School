work_time = int(input("Número de horas trabalhadas: "))
if work_time <= 40:
    salary = work_time * 15
else:
    salary = 600 + ((work_time-40) * 21)
print(f"O salário será {salary}")