import numpy as np
def create_identity_matrix(n):
    arr=np.eye((n))
    return arr

n=int(input("enter row of array"))

print(create_identity_matrix(n))