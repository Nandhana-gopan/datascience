import matplotlib.pyplot as plt
import numpy as np
temp=np.array([12,14,16,18,20,22,24])
sales=np.array([100,200,250,400,300,450,500])
plt.plot(temp,sales,linestyle="-",marker="d",markersize="10",markerfacecolor="black",color="blue")
plt.xlabel("Temperature(deg)")
plt.ylabel("Sales")
plt.title("Sales graph")
plt.show()