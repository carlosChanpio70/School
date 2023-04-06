def insertSort(list):
    N=len(list)
    counter=0
    for i in range(1,N):
        a=list[i]
        j=i-1
        while j>=0 and list[j] >= a:
            list[j+1]=list[j]
            j=j-1
            counter+=1
        list[j+1]=a
    return list,counter

print(insertSort([2,5,9,22,1]))
print(insertSort([1,2,5,9,22]))
print(insertSort([22,9,5,2,1]))
print(insertSort([22,9,1,2,5]))