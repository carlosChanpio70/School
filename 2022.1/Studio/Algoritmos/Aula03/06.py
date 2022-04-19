import datetime
birth = int(input("Digite o ano de nascimento: "))
date_ = datetime.datetime.now()
age = date_.year-birth
print(f"A sua idade é de: {age} anos")
if age <= 3:
    age_scale = "Bebe"
if age > 3:
    age_scale = "Criança"
if age > 10:
    age_scale = "Adolescente"
if age > 18:
    age_scale = "Adulto"
if age > 50:
    age_scale = "Idoso"
print(f"Voce é um(a): {age_scale}")