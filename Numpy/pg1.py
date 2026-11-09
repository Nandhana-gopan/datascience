import numpy as np
#creating arrays
arr1=np.array([1])        
arr2=np.array([1,2,3])
arr3=np.array([[1,2,3],[4,5,6],[3,6,7]])
arr4=np.array([[[10,20,30],[40,50,60]],[[11,22,33],[44,55,66]]])
print(arr1,arr2)
print(arr4)
#checking dimensions
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
#array indexing
print("sum of elements in the array:",arr2[0]+arr2[1]+arr2[2])
#accesssing elements from 2d and 3d arrays
print(arr3[1,1])#printing 5 from arr3
print(arr4[1,0,1])#printing 22 from array4
print(arr4[1,1,-1])
#array slicing
print(arr2[::-1])
print(arr2[:2])
print(arr3[2,1:])
print(arr4[0,1,1:])
#data type checking
fruits=np.array(["apple","banana","kiwi"])
print(fruits.dtype)
#shape
print(arr2.shape)
print(arr3.shape)
print(arr4.shape)