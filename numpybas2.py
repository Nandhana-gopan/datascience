#element wise comparison of 2 given arrays.
import numpy as np
array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 10, 15, 20])

print("Array 1:", array1)
print("Array 2:", array2)

print("\nElement-wise comparison:")

print("Equal to       :", np.equal(array1, array2))
print("Greater than   :", np.greater(array1, array2))
print("Greater or equal:", np.greater_equal(array1, array2))
print("Less than      :", np.less(array1, array2))
print("Less or equal  :", np.less_equal(array1, array2))