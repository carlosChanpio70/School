def main(list):
    count=len(list);r_list=[];i=count-1
    while len(r_list)<count:    
        smol=list[i]
        for n in list:
            if smol>n:
                smol=n
        list.remove(smol)
        r_list.append(smol)
        i-=1
    return r_list

print(main([5,4,14,3,5]))