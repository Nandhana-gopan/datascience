from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score,normalized_mutual_info_score,silhouette_score

import matplotlib.pyplot as plt

iris=load_iris()
X=iris.data[:,:2]
y=iris.target

model=KMeans(n_clusters=3,random_state=45,n_init=10)

model.fit(X)

labels=model.labels_

print("Inertia:",model.inertia_)
print("Adjusted rand Index:",adjusted_rand_score(y,labels))
print("Silhouette_score:",silhouette_score(X,labels))
print("Normalized mutual information:",normalized_mutual_info_score(y,labels))

plt.subplot(1,2,1)
plt.scatter(X[:,0],X[:,1],c=y,cmap="prism")
plt.title("Actual")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

plt.subplot(1,2,2)
plt.scatter(X[:,0],X[:,1],c=labels,cmap="prism")
plt.title("Predicted")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

plt.tight_layout()
plt.show()
