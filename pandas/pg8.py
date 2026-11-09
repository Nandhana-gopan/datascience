import pandas as pd
data={
    "name":["Anu","Arya","Diya","Sana","Preethi"],
    "age":[21,18,19,24,25],
    "marks":[80,89,90,90,87]
}
df=pd.DataFrame(data)
print(df)
print(df.iloc[:,[0,2]])