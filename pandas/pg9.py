import pandas as pd
data={
    "name":["Anu","Arya","Diya","Pravi","Aryan"],
    "occupation":["Teacher","Doctor","Teacher","Doctor","Doctor"],
    "salary":[30000,70000,40000,80000,75000]
}
df=pd.DataFrame(data)
avg_sal=df.groupby("occupation")["salary"].mean()
print(avg_sal)
max_sal=df.groupby("occupation")["salary"].max()
print(max_sal)