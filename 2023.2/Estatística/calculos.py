import math
import scipy.stats as stats

def getfrequencia(y=[]):
    x = 0
    for i in y:
        x += i
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
    median = sorted(y)[len(
        y) // 2] if len(y) % 2 == 1 else (y[len(y) // 2 - 1] + y[len(y) // 2]) / 2.0
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


def getProbabilidade(Total, Número, Probabilidade, tipo_evento):
    Probabilidade /= 100  # Probabilidade em %

    # Calcula o coeficiente binomial (n choose k)
    coeficiente_binomial = math.comb(Total, Número)

    # Calcula a probabilidade
    probabilidade = coeficiente_binomial * \
        (Probabilidade ** Número) * ((1 - Probabilidade) ** (Total - Número))

    if tipo_evento == 0:  # exato x
        resultado = probabilidade
    elif tipo_evento == 1:  # ao menos x/x ou mais/no minimo x
        resultado = sum(probabilidade * (Probabilidade ** k) *
                        ((1 - Probabilidade) ** (Total - k)) for k in range(Número, Total + 1))
    elif tipo_evento == 2:  # no maximo x
        resultado = sum(probabilidade * (Probabilidade ** k) *
                        ((1 - Probabilidade) ** (Total - k)) for k in range(Número))

    print(f"{resultado * 100:.4f}%")


def calculate_probabilities(mean, std_dev, questions):
    for question, value in questions:
        if question == 'less_than':
            z_score = (value - mean) / std_dev
            probability = 0.5 * (1 + math.erf(z_score / math.sqrt(2))) * 100
            print(
                f"Probabilidade de ser menor que {value}: {probability:.2f}%")
        elif question == 'more_than':
            z_score = (value - mean) / std_dev
            probability = (
                1 - (0.5 * (1 + math.erf(z_score / math.sqrt(2))))) * 100
            print(
                f"Probabilidade de ser maior que {value}: {probability:.2f}%")
        elif question == 'between':
            lower_z_score = (value[0] - mean) / std_dev
            upper_z_score = (value[1] - mean) / std_dev
            lower_prob = 0.5 * (1 + math.erf(lower_z_score / math.sqrt(2)))
            upper_prob = 0.5 * (1 + math.erf(upper_z_score / math.sqrt(2)))
            probability = (upper_prob - lower_prob) * 100
            print(
                f"Probabilidade de estar entre {value[0]} e {value[1]}: {probability:.2f}%")
        else:
            print("Tipo de pergunta não reconhecido.")


#mean = 77
#std_dev = 11.6

#questions = [
#    ('less_than', 60),
#    ('more_than', 90),
#    ('between', (60,90)),
#]

#calculate_probabilities(mean, std_dev, questions)

def intervalo_confianca(amostra_media, desvio_padrao_populacional, tamanho_amostra, nivel_confianca):
    # Calcula o erro padrão da média
    erro_padrao_media = desvio_padrao_populacional / math.sqrt(tamanho_amostra)

    # Calcula o intervalo de confiança
    valor_critico = stats.norm.ppf(1 - (1 - nivel_confianca) / 2)
    limite_inferior = amostra_media - valor_critico * erro_padrao_media
    limite_superior = amostra_media + valor_critico * erro_padrao_media

    print(f"Intervalo de Confiança de {nivel_confianca * 100}%: {limite_inferior:.2f} < µ < {limite_superior:.2f}")

# Dados do problema
amostra_media = 1800
desvio_padrao = 140
tamanho_amostra = 26
nivel_confianca = 0.95

intervalo_confianca(amostra_media, desvio_padrao, tamanho_amostra, nivel_confianca)