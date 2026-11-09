import pandas as pd
print("enter the numbers:")
lst=list(map(int,input().split()))
ser=pd.Series(lst)
print(ser)