import numpy as np
def array_strides(n):
    arr=np.array([i for i in range(0,n)])
    return arr.strides

n=int(input("enter size of array"))
print(array_strides(n))