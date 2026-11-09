import matplotlib.pyplot as plt
import numpy as np
x=np.array(["jan","feb","march","apr","may"])
high=np.array([40,38,37,39,38])
low=np.array([25,27,23,26,27])
plt.plot(x,low,linestyle="-",color="red",marker=".",markerfacecolor="green",markersize=5,label="Lowest temperature")
plt.plot(x,high,linestyle="-",color="blue",marker=".",markerfacecolor="red",markersize=5,label="Highest temperature")
plt.xlabel("Month")
plt.ylabel("temperature")
plt.title("Temperature graph")
plt.legend()
plt.show()