def get_sum(n):
    nr = 0
    for I in range(1, n+1):
        nr += 1/I
    return nr

print(get_sum(5))
