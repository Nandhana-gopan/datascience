import matplotlib.pyplot as plt
import  numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix

iris=load_iris()

X=iris.data
Y=iris.target

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.75,random_state=11)

model=DecisionTreeClassifier(criterion="entropy",max_depth=4,min_samples_leaf=2)

model.fit(X_train,Y_train)
my_pred=model.predict(X_test)

print("Accuracy score:",accuracy_score(Y_test,my_pred))
print("Confusion matrix:",confusion_matrix(Y_test,my_pred))
print("Classification report :",classification_report(Y_test,my_pred,target_names=iris.target_names))

sample=np.array([[2.2,3.4,1.4,3.1]])
result=model.predict(sample)

print("The flower belongs to:",iris.target_names[result[0]])

plt.subplot(1,2,1)
plt.scatter(X_test[:,0],X_test[:,1],c=Y_test,cmap="viridis")
plt.title("Actual")
plt.xlabel("Sepal Length")
plt.ylabel("sepal width")

plt.subplot(1,2,2)
plt.scatter(X_test[:,0],X_test[:,1],c=my_pred,cmap="viridis")
plt.title("Predicted")
plt.xlabel("Sepal Length")
plt.ylabel("sepal width")

plt.tight_layout()
plt.show()

plot_tree(model,feature_names=iris.feature_names,class_names=iris.target_names,filled=True)
plt.title("Decision tree")
plt.show()