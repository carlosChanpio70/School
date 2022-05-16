def main(list):
    negatives=0
    for i in list:
        if i<0:
            negatives+=1
    return negatives

print(main([1,-1,-5,4,-5]))