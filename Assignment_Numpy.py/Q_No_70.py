import numpy as np
arr=np.array([10,20,30,40,50])

print(np.extract(arr>=20 and arr<=40,arr))