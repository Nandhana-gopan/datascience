import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
lows=np.array([22,23,27,26,21])
highs=np.array([35,37,40,38,49])
plt.subplot(1,2,1)
plt.plot(x,lows,linestyle="-",color="yellow",marker="*",markersize="8",markerfacecolor="green",label="Lows")
plt.title("Lows")
plt.xlabel("day")
plt.ylabel("temp")
plt.legend()
plt.subplot(1,2,2)
plt.plot(x,highs,linestyle="-",color="red",marker="*",markersize="8",markerfacecolor="green",label="Highs")
plt.title("Highs")
plt.xlabel("day")
plt.ylabel("temp")
plt.legend()
plt.suptitle("Graph")
plt.show()


