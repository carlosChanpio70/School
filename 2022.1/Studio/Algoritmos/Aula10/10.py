def main(list):
    loop=0
    size = len(list)
    while loop<size:
        if list[loop]<0:
            list[loop]=0
        loop+=1
    return list

print(main([5,-15,4,-5,0]))