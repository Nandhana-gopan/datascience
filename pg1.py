from sklearn.datasets import load_iris
import numpy as np
from sklearn.model_selection import train_test_split #train and test data splitting
from sklearn.naive_bayes import GaussianNB #model used
#different matrices
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report 
iris=load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)#random state=to avoid random splitting of dataset
model=GaussianNB()
model.fit(X_train,y_train) #to feed training data into the model
y_prediction=model.predict(X_test)
print(y_prediction)
print(y_test)
print("accuracy score:",accuracy_score(y_test,y_prediction))
print("confusion matrix:",confusion_matrix(y_test,y_prediction))
print("classification report:",classification_report(y_test,y_prediction))
sample=np.array([[4.9,3.0,1.4,0.2]])
prediction = model.predict(sample)

print("Predicted class:", prediction[0])
print("Predicted flower:", iris.target_names[prediction[0]])
#implement gaussian np using the public dataset load_breast_cancer