import matplotlib.pyplot as plt
import numpy as np
a=np.array([2,3,4,5])
b=np.array([7,8,9,0])
color=['red','blue','green']
#plt.scatter(a,b,s=100,c='black',label='cluster 1')
#plt.plot(a,color='blue',linewidth=3,linestyle='dashed')
#plt.grid(axis='x',color='red',linewidth=4)
#plt.subplot(1,2,2)
#plt.scatter(a,b,color='black')
plt.scatter(a,b,c=color)
plt.colorbar()

plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.title(a,loc='left')
plt.show()