import pandas as pd
data=[["A",25,80],
      ["B",24,89],
      ["C",26,100]]
df=pd.DataFrame(data,columns=["Student","Age","Marks"])
print(df)