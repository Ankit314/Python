import numpy as np
a=np.array([[3,4,5],[9,8,7]])
b=a.ravel()
b=b.reshape((2,3))
print(b)
