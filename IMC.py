IMC_mulheres = [19.1,25.8,27.3,32.3]
IMC_homens = [20.7,26.4,27.8,31.1]

def IMC(genero,peso,altura):
    if genero == "m":
        lista_imc = [20.7,26.4,27.8,31.1]
    else:
        lista_imc = [19.1,25.8,27.3,32.3]
    imc = peso/altura**2
    if (imc<lista_imc[0]):
        return f"Abaixo do peso, com IMC de {imc}"
    if (imc<lista_imc[1]):
        return f"No peso normal, com IMC de {imc}"
    if (imc<lista_imc[2]):
        return f"Marginalmente acima do peso, com IMC de {imc}"
    if (imc<lista_imc[3]):
        return f"Acima do peso ideal, com IMC de {imc}"
    else:
        return f"Obeso, com IMC de {imc}"