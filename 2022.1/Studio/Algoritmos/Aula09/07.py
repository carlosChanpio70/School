def somarIntervalo(n1,n2):
    nr=0
    if n2<n1:
        return somarIntervalo(n2,n1)
    for I in range(n1,n2):
        nr+=I
    return nr

print(somarIntervalo(5,10))