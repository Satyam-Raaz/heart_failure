l=[1,2,3]

def sum_cubes(l):
    sum=0
    for i in l:
        sum+=i*i*i     

    return sum    


print(sum_cubes(l))