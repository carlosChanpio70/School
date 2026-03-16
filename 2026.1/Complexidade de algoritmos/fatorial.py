import time

def factorial(n):
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            print(f"Calculando {i}! = {result} * {i}!")
            result *= i
        return result
    
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        print(f"Calculando {n}! = {n} * {n-1}!")
        return n * factorial_recursive(n - 1)
    
time_start = time.time()
print(f"Resultado de fatorial 5: {factorial(5)}")
time_end = time.time()
print(f"Tempo de execução do fatorial: {time_end - time_start:.6f} segundos")

time_start = time.time()
print(f"Resultado de fatorial recursivo 5: {factorial_recursive(5)}")
time_end = time.time()
print(f"Tempo de execução do fatorial recursivo: {time_end - time_start:.6f} segundos")