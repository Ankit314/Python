import numpy as np
a=np.array([1,0,0,1,0],dtype=bool)
b=np.array([0,0,1,1,0],dtype=bool)
print(np.logical_and(a,b))
