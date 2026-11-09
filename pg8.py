#write a pyhton program:
#1.Read number of rows and columns
#2.create matrix 1
#3.another matrix
#find dot product,transpose of both,trace of both,rank of both , determinant of mat1,inverse of matrix2
import numpy as np
rows=int(input("enter the number of rows of matrix :"))
cols=int(input("enter the number of columns of matrix :"))
matrix1=[]
for i in range(rows):
    print("enter the elements:")
    row=list(map(int,input().split()))
    matrix1.append(row)
matrix1=np.array(matrix1)
print(matrix1)
matrix2=[]
for i in range(rows):
    print("enter the elements:")

