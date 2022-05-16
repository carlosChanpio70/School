def main(list):
    smallest=list[0]
    for i in list:
        if smallest>i:
            smallest=i
    return smallest

print(main([5,15,25,4,12]))