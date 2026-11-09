import matplotlib.pyplot as plt
import numpy as np
group=np.array([1,2,3,4])
men=np.array([25,30,35,40])
wom=np.array([40,45,50,55])
bar_width=0.35
plt.bar(group-bar_width,men,color="blue")
plt.bar(group+bar_width,wom,color="pink")
plt.show()