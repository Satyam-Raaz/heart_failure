import numpy as np
def item_size_info(n):
    arr=np.array([i for i in range(0,n)])
    return arr.size,arr.byteswap()

n=int(input("enter size of array"))
print(item_size_info(n))