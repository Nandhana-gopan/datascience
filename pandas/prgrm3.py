import pandas as pd
print("enter the names:")
name=list(map(str,input().split()))
print("enter ages:")
ages=list(map(int,input().split()))
print("enter marks:")
mark=list(map(int,input().split()))
data={
    "Name":name,
    "Age":ages,
    "Marks":mark
}
df=pd.DataFrame(data,index=[1,2,3])
print(df)
print(df.info)
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.describe())