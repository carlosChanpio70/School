def produto(a, b):
    if b == 1:
        return a
    return produto(a, (b-1))+a


def interactive_sum(a):
    n = 0
    for i in range(len(a)-1, -1, -1):
        n += a[i]
    return n


def sum(a):
    def body(a, i):
        if i < 0:
            return 0
        return a[i]+body(a, i-1)
    return body(a, len(a)-1)


def tail_sum(a):
    def body(a, i, s):
        if i < 0:
            return s
        return body(a, i-1, s+a[i])
    return body(a, len(a)-1, 0)


def max(a):
    def body(a, i, j):
        if i == j:
            return a[i]
        mid = (i+j)//2
        x = body(a, i, mid)
        y = body(a, mid+1, j)
        return x if (x > y) else y
    return body(a, 0, len(a)-1)