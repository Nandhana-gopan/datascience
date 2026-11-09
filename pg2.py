from sklearn.datasets import load_breast_cancer
import numpy as np
from sklearn.model_selection import train_test_split #train and test data splitting
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report 
cancer = load_breast_cancer()
X=cancer.data
y=cancer.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
#random state = to avoid random splitting of dataset
model=GaussianNB()
model.fit(X_train,y_train)#to feed training data into the model
y_prediction=model.predict(X_test)
print(y_prediction)
print(y_test)
print("accuracy score:",accuracy_score(y_test,y_prediction))
print("confusion matrix:",confusion_matrix(y_test,y_prediction))
print("classification report:",classification_report(y_test,y_prediction))
sample=X_test[18].reshape(1,-1)
prediction=model.predict(sample)
print("predicted classes:",cancer.target_names[prediction])
