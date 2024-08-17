import numpy as np
input_matrix=np.array([[1,2,3],[4,5,6]])

def func(arr):
    return arr.flatten()

print(func(input_matrix))