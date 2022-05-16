def main(list):
    sum = 0
    size = 0
    for i in list:
        sum += i
        size += 1
    return sum/size

print(main([5, 10, 15]))