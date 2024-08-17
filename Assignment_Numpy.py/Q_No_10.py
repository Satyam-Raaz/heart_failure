import numpy as np
def shape_stride_relationship(n):
    arr=np.array([i for i in range(0,n)])
    return arr.shape,arr.strides

n=int(input("enter size of array"))
print(shape_stride_relationship(n))