def contarImpar(n1,n2,odd=0):
    if n2<n1:
        return contarImpar(n2,n1,odd)
    for i in range(n1,n2):
        if i%2!=0:
            odd+=1
    return odd

print(contarImpar(1,150))
print(contarImpar(100,1))