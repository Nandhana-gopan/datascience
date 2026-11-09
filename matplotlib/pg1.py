import matplotlib.pyplot as plt
import numpy as np
x_data=np.array([1,2,6,18])
y_data=np.array([3,10,12,20])
plt.plot(x_data,y_data,color="red",marker="*",markersize="10",linestyle=":",markerfacecolor="green")
plt.title("My line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()