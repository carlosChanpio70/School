def main(list):
    biggest=list[0]
    for i in list:
        if biggest<i:
            biggest=i
    return biggest

print(main([5,15,25,4,12]))