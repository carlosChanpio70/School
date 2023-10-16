import math

def getfrequencia(y=[]):
    x=0
    for i in y:
        x+=i
    for i in y:
        print(f"{i}/{x}*100={i/x*100:.2f}%")
    print(x)

def getestatistica(y=[]):
    if not y:
        print("The input list is empty.")
        return

    # Calculate the statistics
    mean = sum(y) / len(y)
    mode = max(set(y), key=y.count)
    median = sorted(y)[len(y) // 2] if len(y) % 2 == 1 else (y[len(y) // 2 - 1] + y[len(y) // 2]) / 2
    amplitude = max(y) - min(y)
    variance = sum((x - mean) ** 2 for x in y) / len(y)
    std_deviation = variance ** 0.5
    coefficient_of_variation = (std_deviation / mean) * 100

    # Print the statistics
    print(f"A) Média Aritmética: {mean:.2f}")
    print(f"B) Moda: {mode:.2f}")
    print(f"C) Mediana: {median:.2f}")
    print(f"D) Amplitude Total: {amplitude:.2f}")
    print(f"E) Variância: {variance:.2f}")
    print(f"F) Desvio Padrão: {std_deviation:.2f}")
    print(f"G) Coeficiente de Variação: {coefficient_of_variation:.2f}%")

import math

def getProbabilidade(Total, Número, Probabilidade, tipo_evento):
    Probabilidade /= 100  # Probabilidade em %
    
    # Calcula o coeficiente binomial (n choose k)
    coeficiente_binomial = math.comb(Total, Número)
    
    # Calcula a probabilidade
    probabilidade = coeficiente_binomial * (Probabilidade ** Número) * ((1 - Probabilidade) ** (Total - Número))
    
    if tipo_evento == 0:#exato x
        resultado = probabilidade
    elif tipo_evento == 1:#ao menos x/x ou mais/no minimo x
        resultado = sum(probabilidade * (Probabilidade ** k) * ((1 - Probabilidade) ** (Total - k)) for k in range(Número, Total + 1))
    elif tipo_evento == 2:#no maximo x
        resultado = sum(probabilidade * (Probabilidade ** k) * ((1 - Probabilidade) ** (Total - k)) for k in range(Número))
    
    print(f"{resultado * 100:.4f}%")

getProbabilidade(9,9,82,0)
getProbabilidade(9,7,82,1)
getProbabilidade(9,6,82,1)
