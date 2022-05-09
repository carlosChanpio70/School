def verificarEstacao(dia,mes):
    if (12<=mes and 21<=dia) or(mes<=3 and dia<21):
        return "verão"
    if (3<=mes and 21<=dia) or(mes<=6 and dia<21):
        return "outono"
    if (6<=mes and 21<=dia) or(mes<=9 and dia<23):
        return "inverno"
    if (9<=mes and 23<=dia) or(mes<=12 and dia<21):
        return "primavera"
    return "Valor inválido"

print(verificarEstacao(5,2))