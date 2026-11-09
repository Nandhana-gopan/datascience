import numpy as np
arr=np.array([1,2,3,4])    #list
print(arr)
arr2=np.array([[1,2,3],[4,5,6]])#nested list
print(arr2)
arr3=np.array((1,2,3,4,5))    #tuple
print(arr3)
print(arr3*5)    #adding,multiplying... elements
print(type(arr2))
floatarray=np.array([1,2.5,3.0])
stringarray=np.array(("apple","banana","orange"))
print(stringarray)
boolarray=np.array([True,False,True])
print(boolarray)
print(arr2.shape)    #rows,column
print(arr2.size)          #total number of elemnts
print(arr2.ndim)              #number of dimensions(1-d,2-d,3-d....)
print(floatarray.dtype)               #type of array