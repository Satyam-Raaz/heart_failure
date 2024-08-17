l=[1,2,5,8]

def odd_double(l):
    n=len(l)
    l1=[]
    for i in l:
        if i%2!=0:
            l1.append(i+i)

    return l1        


print(odd_double(l))