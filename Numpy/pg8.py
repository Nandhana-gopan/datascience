import numpy as np
array=np.random.randint(1,10,8)
print(array)
num=int(input("Enter the number to search for:"))
if num in array:
    print("Found ")
else:
    print("not found")