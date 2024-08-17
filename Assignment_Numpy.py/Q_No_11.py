import numpy as np
def create_zeros_array(n):
    arr=np.zeros((n))
    return arr

n=int(input("enter size of array"))
print(create_zeros_array(n))