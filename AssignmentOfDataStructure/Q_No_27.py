t=(1,2,3,4,5)

def func(t):
    max=-1
    for i in t:
        if i>max:
            max=i
    print(max)
    min=t[0]

    for i in t:
        if  i<min:
            min=i 

    print(min)               

func(t)


