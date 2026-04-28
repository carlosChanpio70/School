import csv
import random
import time

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def write_csv(collumn1, collumn2,data1, data2):
    data1=str(data1)
    data2=str(data2)
    data = []

    # Read existing data from CSV file
    try:
        with open('resultados_ordenacao.csv', 'r', newline='') as file:
            data = [line.strip() for line in file]
    except FileNotFoundError:
        pass
    
    overwritten=False
    for i, line in enumerate(data):
        if data1 in line:
            data[i:i+1] = ["tamanho: "+data1, "tempo: "+data2]
            overwritten=True
            
    if not overwritten:
        data.extend(["tamanho: "+data1, "tempo: "+data2])

    # Write data to CSV file
    with open('resultados_ordenacao.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for line in data:
            writer.writerow([line])
        
    

def array_test(size):
    array = [x for x in range(size)]
    random.shuffle(array)
    time_start = time.time()
    selection_sort(array)
    time_end = time.time()
    executed_time = time_end - time_start
    write_csv("tamanho","tempo",size,executed_time)    

array_test(5000)
array_test(10000)
array_test(25000)
array_test(50000)