import numpy as np
arr=np.array([[1,2,3],[4,5,6]])

print(np.sum(arr%2==0,axis=0))