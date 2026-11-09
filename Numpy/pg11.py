import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
total_sum=np.sum(arr)
col_sum=np.sum(arr,axis=0)
row_sum=np.sum(arr,axis=1)
print("sum of elemnts:",total_sum)
print("column_wise sum:",col_sum)
print("row_wise sum:",row_sum)