import matplotlib.pyplot as plt
import pandas as pd

from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

data=pd.read_csv("students.csv")

X=data[["attendance","internal","assignment"]]
Y=data["result"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20,random_state=12,stratify=Y)

model=DecisionTreeClassifier(criterion="entropy",max_depth=4,min_samples_leaf=2)
model.fit(X_train,Y_train)

y_pred=model.predict(X_test)

print("Accuracy score:",accuracy_score(Y_test,y_pred))
print("Confusion matrix:",confusion_matrix(Y_test,y_pred,labels=["pass","fail"]))
print("classification report:",classification_report(Y_test,y_pred,labels=["pass","fail"]))

sample=pd.DataFrame([[75,10,2]],columns=["attendance","internal","assignment"])
result=model.predict(sample)

print("The student will:",result[0])

actual=Y_test.map({"pass":0,"fail":1})
predicted=pd.Series(y_pred).map({"pass":0,"fail":1})
plt.subplot(1,2,1)
plt.scatter(X_test["internal"],X_test["assignment"],c=actual,cmap="coolwarm")
plt.title("Actual")
plt.xlabel("Internal")
plt.ylabel("Assignment")

plt.subplot(1,2,2)
plt.scatter(X_test["internal"],X_test["assignment"],c=predicted,cmap="coolwarm")
plt.title("Predicted")
plt.xlabel("Internal")
plt.ylabel("Assignment")

plt.tight_layout()
plt.show()

plot_tree(model,feature_names=["attendance","internal","assignment"],class_names=model.classes_,filled=True)
plt.title("decision tree")
plt.show()