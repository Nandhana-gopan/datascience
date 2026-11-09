#create a vector/matrix from 0-20.change the sign of the numbers from 9-15
import numpy as np
vector=np.arange(1,21)
for i in range(9,16):
    vector[i]=-vector[i]
print(vector)