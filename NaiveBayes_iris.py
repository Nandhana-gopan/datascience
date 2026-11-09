from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=12)
model=GaussianNB()
model.fit(x_train,y_train)
y_predict=model.predict(x_test)
accuracy=accuracy_score(y_test,y_predict)
report=classification_report(y_test,y_predict,target_names=iris.target_names)
print("Accuracy score: ",accuracy)
print("CLASSIFICATION REPORT:\n",report)
print("confusion matrix:\n",confusion_matrix(y_test,y_predict))

sample=np.array([[1.2,2.3,4.5,4]])
pred=model.predict(sample)
print("predicted class:",iris.target_names[pred])

plt.subplot(1,2,1)
plt.scatter(x_test[:,0],x_test[:,1],c=y_test)
plt.title("Actual classification")
plt.ylabel("sepal width")
plt.xlabel("sepal length")

plt.subplot(1,2,2)
plt.scatter(x_test[:,0],x_test[:,1],c=y_predict)
plt.title(" Predicted classification")
plt.ylabel("sepal width")
plt.xlabel("sepal length")
plt.show()