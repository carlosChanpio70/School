def selectSort(list):
    N=len(list)
    counter=0
    for i in range(0,N-1):
        p=i
        for j in range(i+1,N):
            if list[j]<list[p]:
                p=j
        k=list[i]
        list[i]=list[p]
        list[p]=k
        counter+=1
    return list,counter

print(selectSort([2,5,9,22,1]))
print(selectSort([1,2,5,9,22]))
print(selectSort([22,9,5,2,1]))
print(selectSort([22,9,1,2,5]))
