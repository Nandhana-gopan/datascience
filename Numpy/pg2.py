import numpy as np
n=int(input("enter the number of values:"))
fh=[]
for i in range (n):
   fh.append(float(input()))
fh=np.array(fh)
print(fh)
cg=[]
for value in fh:
   value=(value-32)*(5/9)
   cg.append(value)
cg=np.array(cg)
print("Converted:",cg)