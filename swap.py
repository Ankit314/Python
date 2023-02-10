import numpy as np
x=np.arange(12).reshape(3,4)
print("original array :")
print(x)
y=x[:,[0,1]]=x[:,[1,0]]
print("\nAfter swapping arrays:")
print(y)


