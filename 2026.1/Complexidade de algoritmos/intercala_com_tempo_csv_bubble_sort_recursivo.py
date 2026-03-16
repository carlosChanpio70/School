import csv, time, numpy as np
from random import seed
from random import random

def bubble_sort(arr, op):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    if op == "D":
        arr.reverse()
    
    return arr

def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# seed random number generator
seed(1)
# generate random numbers between 0-1 in vector_1
vector_1=[]
for x in range(100):
    vector_1.append(random())


# generate random numbers between 0-1 in vector_2
vector_2=[]
for x in range(100):
    vector_2.append(random())

#Definition of new_vector vector, used for processing operations bellow
size_vector_1 = len(vector_1)
size_vector_2 = len(vector_2)

new_vector = []

for i in range(size_vector_1):
    new_vector.append(vector_1[i])

for i in range(size_vector_2):
    new_vector.append(vector_2[i])

f = open('intercala_com_tempo_csv.csv', 'w', newline='')
writer = csv.writer(f, delimiter=',')

writer.writerow(np.array(["Type_Of_Execution", "Time"]))

#First operation. ID 1. Ascending sort
start = time.time()

#Code of first operation
new_vector=bubble_sort(new_vector,"A")

end = time.time()
final_time = end - start

writer.writerow(["Ascending sort", final_time])

#Second operation. ID 2. Descending sort
start = time.time()

new_vector=bubble_sort(new_vector, "D")

end = time.time()
final_time = end - start

writer.writerow(["Descending sort", final_time])

#Third operation. ID 3. Binary search for a random number between 0-1
vector_3 = []
for i in range(10000):
    vector_3.append(random())
    
start = time.time()
vector_3 = bubble_sort(vector_3, "A")
end = time.time()
final_time = end - start

writer.writerow(["Large dataset (10,000)", final_time])

time_array = []
for i in range(10):
    x = random()
    start = time.time()
    result = binary_search(vector_3, x)
    end = time.time()
    time_array.append(end - start)
    print(f"Binary search for {x} found at index {result} in {end - start} seconds")

average_time = sum(time_array) / len(time_array)
print(f"Average time for binary search: {average_time} seconds")
writer.writerow(["Binary search (10,000 elements)", average_time])

# close the file
f.close()