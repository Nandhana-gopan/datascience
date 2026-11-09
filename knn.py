import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

iris=load_iris()

X=iris.data
Y=iris.target

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=45)

model=KNeighborsClassifier(n_neighbors=5)

model.fit(X_train,Y_train)

y_pred=model.predict(X_test)

print("Accuracy score:",accuracy_score(Y_test,y_pred))
print("confusion matrix:",confusion_matrix(Y_test,y_pred))
print("classification Report:",classification_report(Y_test,y_pred,target_names=iris.target_names))

new_sample=np.array([[1.2,2.2,3,2.7]])
result=model.predict(new_sample)

print("New sample belongs to :",iris.target_names[result])

plt.subplot(1,2,1)
plt.scatter(X_test[:,2],X_test[:,3],marker="*",c=Y_test,cmap="viridis",label="actual")
plt.title("Actual")
plt.xlabel("Petal length")
plt.ylabel("petal width")
plt.legend()

plt.subplot(1,2,2)
plt.scatter(X_test[:,2],X_test[:,3],marker="*",c=y_pred,cmap="viridis",label="predicted")
plt.title("Predicted")
plt.xlabel("Petal length")
plt.ylabel("petal width")
plt.legend()

plt.tight_layout()
plt.show()