import numpy as np
arr1=np.ones((3,4))
arr2=np.ones((4,3))
def func(arr1,arr2):
    print(np.concatenate(arr1,arr2))

func(arr1,arr2)
