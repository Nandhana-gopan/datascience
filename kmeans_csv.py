import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,adjusted_rand_score,normalized_mutual_info_score

data=pd.read_csv("kmeansdata.csv")

X=data[["annualincome","spendingscore"]]

scalar=StandardScaler()
X_scaled=scalar.fit_transform(X)

model=KMeans(n_clusters=3,random_state=11,n_init=10)
model.fit(X_scaled)

labels=model.labels_

print("Silhoutee score:",silhouette_score(X_scaled,labels))
print("Inertia:",model.inertia_)

plt.scatter(X["annualincome"],X["spendingscore"],c=labels,cmap="prism")
plt.title("Clustering graph")
plt.xlabel("Annual income")
plt.ylabel("Spending score")
plt.show()