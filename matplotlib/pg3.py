import matplotlib.pyplot as plt
import numpy as np
data=np.loadtxt(r"C:\Users\nandh\OneDrive\Desktop\datasciencelab\matplotlib\samplefile.txt")
x=data[:,0]
y=data[:,1]
plt.plot(x,y,linestyle=":",color="black",marker="*",markerfacecolor="red",markersize=5)
plt.xlabel("x")
plt.ylabel("y")
plt.show()