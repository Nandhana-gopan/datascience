import numpy as np
arr=np.array([1,2,3,4,5,6])#to create array
print(arr)
print(arr.shape)
#reshape
a1=arr.reshape(2,3) #2 rows 3 columns
print(a1)
print(a1.shape)
a2=np.array([10,20,30,40])
print(a2)
print(a2.shape)
reshaped=a2.reshape(4,1)
print(reshaped)
print(a2.reshape(1,-1))#1->make the array have one row ,,-1->automatically calculates the number of columns
a3=np.array([10,20,30,40,50,60])
print(a3)
print(a3.shape)
a4=a3.reshape(1,-1)
print(a4)
print(a4.shape)