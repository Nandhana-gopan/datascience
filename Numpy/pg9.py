import numpy as np
array=np.array([10,20,30,40])
print("writing the array into the file.........")
np.savetxt(fname="sample.txt",X=array,fmt="%d")
print("loading the contents:")
contents=np.loadtxt(fname="sample.txt")
print(contents)