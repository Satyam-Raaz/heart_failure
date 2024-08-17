l=[1,2,5,8]

def sq_even(l):
    n=len(l)
    l1=[]
    for i in l:
        if i%2==0:
            l1.append(i**2)

    return l1        


print(sq_even(l))
