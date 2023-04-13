def bubbleSort(list):
    counter=0
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            counter+=1
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list,counter

print(bubbleSort([2,9,5,22,1]))
print(bubbleSort([22,2,5,9,1]))
print(bubbleSort([22,9,5,2,1]))
print(bubbleSort([22,9,1,2,5]))
