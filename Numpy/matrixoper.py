import numpy as np
n=int(input("Enter the order of square matrices:"))
a=[]
for i in range(n):
    row1=list(map(float,input().split()))
    a.append(row1)
b=[]
for i in range(n):
    row2=list(map(float,input().split()))
    b.append(row2)
a=np.array(a)
b=np.array(b)

print("Dot product:")
print(np.dot(a,b))
print("Transpose:")
print(np.transpose(a))
print("Trace:")
print(np.trace(b))
print("Rank of matrix a:")
print(np.linalg.matrix_rank(a))
print("Determinant of a:")
print(np.linalg.det(a))
if np.linalg.det!=0:
    print("Inverse:",np.linalg.inv(a))
else:
    print("Incverse does not exist")
eigenval,eigenvect=np.linalg.eig(a)
print("Eigenvalues:",eigenval)
print("EigenVectors:",eigenvect)
