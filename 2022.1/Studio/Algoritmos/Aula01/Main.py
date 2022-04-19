#Info input
name = input("Qual o seu nome? ")
age = int(input(f"{name}, qual a sua idade? "))
gender = input(f"{name}, qual o seu genero? ")
#Gender logic
if gender == "masculino":
    Welcome = "Bem vindo"
if gender == "feminino":
    Welcome = "Bem vinda"
if gender == "outro":
    Welcome = "Bem vinde"
print(f"{Welcome}: {name}\nIdade: {age} anos.")
#Age logic
if age <= 12:
    age_scale = "Criança"
if age > 12:
    age_scale = "Adolescente"
if age > 18:
    age_scale = "Adulto"
if age > 60:
    age_scale = "Idoso"
print(f"Voce é um(a): {age_scale}")
print("Primeira aula de algoritmos!")#Noreasontobehere print
