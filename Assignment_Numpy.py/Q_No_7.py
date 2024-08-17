import numpy as np
def array_dimension(n):
    arr=np.array([i for i in range(0,n)])
    return arr.ndim

n=int(input("enter size of array"))
print(array_dimension(n))