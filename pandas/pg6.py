import pandas as pd
data={
    "name":["Anu","Arya","Diya"],
    "age":[21,18,19],
    "marks":[80,89,90]
}
df=pd.DataFrame(data)
sorted_data=df.sort_values(by=["age","name"],ascending=[True,True])
print(sorted_data)