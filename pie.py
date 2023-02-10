import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
y=np.array(["apple","banana","orange","pine","mango"])
z=np.array([0.2,0.2,0.2,0.2,0.2])
w=np.array(["red","green","yellow","blue","pink"])
plt.pie(x,labels=y,startangle=90,explode=z,shadow=True,colors=w,autopct='%1.1f')
plt.legend(loc="upper left",title="fruits",bbox_to_anchor=(0.05,0.3))
#plt.pie(x)
plt.show()

