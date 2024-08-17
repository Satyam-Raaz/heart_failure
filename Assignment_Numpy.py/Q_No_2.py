import numpy as np
arr=np.array([1.5,2.6,3.7])
count=0
n=len(arr)
print(type(arr[0]))
for i in range(0,n):
    if type(arr[i])==np.float64:
        count+=1
if count==len(arr):
    print("data types is float64")


