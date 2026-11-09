import numpy as np
randarr=np.random.randint(1,10,5)
print(randarr)
for i in randarr:
    if i > 4:
        print(i)
#can also use np.where(arr>4)