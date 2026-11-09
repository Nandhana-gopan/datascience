import matplotlib.pyplot as plt
import numpy as np
pg=np.array(["Java","Python","PHP","JavaScript","C#","C++"])
popular=np.array([22.2,17.6,8.8,8,7.7,6.7])
colors=["red","green","orange","pink","blue"]
plt.bar(pg,popular,color=colors)
plt.title("Popularity of Programming Languages")
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.show()