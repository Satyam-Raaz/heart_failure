import numpy as np
def create_ones_array(n,m):
    arr=np.zeros((n,m))
    return arr

n=int(input("enter row of array"))
m=int(input("enter column of array"))

print(create_ones_array(n,m))