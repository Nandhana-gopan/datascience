import pandas as pd
data={
    "name":["Anu","Arya","Diya"],
    "age":[21,18,19],
    "marks":[80,89,90]
}
old_df=pd.DataFrame(data,index=[1,2,3])
print(old_df)
new_df=old_df.reset_index(drop=True)
print(new_df)