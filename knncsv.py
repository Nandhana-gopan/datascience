import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.preprocessing import StandardScaler

data=pd.read_csv("employ.csv")
X=data[["age","year","salary"]]
y=data["joblevel"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=11)

scalar=StandardScaler()

X_train=scalar.fit_transform(X_train)
X_test=scalar.transform(X_test)

model=KNeighborsClassifier(n_neighbors=3)

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("Accuracy score:",accuracy_score(y_test,y_pred))
print("Confusion matrix:",confusion_matrix(y_test,y_pred))
print("Classification report:",classification_report(y_test,y_pred,labels=["junior","mid","senior"]))

sample_data={
    "age":29,
    "year":8,
    "salary":38000
}
sample=pd.DataFrame([sample_data],columns=["age","year","salary"])
sample=scalar.transform(sample)

result=model.predict(sample)

print("The given employee is a :",result[0])

actual=y_test.map({"junior":0,"mid":1,"senior":2})
predicted=pd.Series(y_pred).map({"junior":0,"mid":1,"senior":2})

plt.subplot(1,2,1)
plt.scatter(X_test[:,1],X_test[:,2],c=actual,cmap="viridis",label="Actual")
plt.title("Actual")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.legend()

plt.subplot(1,2,2)
plt.scatter(X_test[:,1],X_test[:,2],c=predicted,cmap="viridis",label="predicted")
plt.title("Predicted")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.legend()

plt.tight_layout()
plt.show()
