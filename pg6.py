#write a program to create a 2d array using numpy and print it
import numpy as np
a=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(a)
b=np.array([[10,20,30],
            [40,50,60],
            [70,80,90]])
print(b)

# print("addition:",a+b)
# print("subtraction:",a-b)
# print("multiplication:",a*b)
c=np.dot(a,b)
print(c)
ta=np.transpose(a)
print(ta)
sample = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])
det = np.linalg.det(sample)

print(det)

inv=np.linalg.inv(sample)
print(inv)