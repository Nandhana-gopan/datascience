import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

breast_cancer=load_breast_cancer()
X=breast_cancer.data
Y=breast_cancer.target

X_train,X_test,y_train,y_test=train_test_split(X,Y,train_size=0.80,random_state=42)

model=GaussianNB()

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("Accuracy score:",accuracy_score(y_test,y_pred))
print("Confusion matrix:",confusion_matrix(y_test,y_pred))
print("Classification report:",classification_report(y_test,y_pred,target_names=breast_cancer.target_names))

sample=X_test[0].reshape(1,-1)
result=model.predict(sample)
print("The patient belongs to category:",result[0])

plt.subplot(1,2,1)
plt.scatter(X_test[:,0],X_test[:,1],c=y_test,cmap="viridis",label="Actual")
plt.title("Actual")
plt.legend()

plt.subplot(1,2,2)
plt.scatter(X_test[:,0],X_test[:,1],c=y_pred,cmap="viridis",label="Predicted")
plt.title("Predicted")
plt.legend()
plt.tight_layout()
plt.show()