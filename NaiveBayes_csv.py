import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

data=pd.read_csv("spamornot.csv")

X=data['Message']
Y=data['Label']

countvector=CountVectorizer()
X=countvector.fit_transform(X)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.80,random_state=43)

model=MultinomialNB()

model.fit(X_train,Y_train)

Y_pred=model.predict(X_test)
print("Accuracy score:",accuracy_score(Y_test,Y_pred))
print("Confusion matrix:",confusion_matrix(Y_test,Y_pred))
print("Classification report:",classification_report(Y_test,Y_pred,labels=["spam","not spam"]))

sample=["Tomorrow u have classes"]
sample=countvector.transform(sample)

result=model.predict(sample)

print("The email is :",result[0])

actual=Y_test.map({"not spam":0,"spam":1})
predicted=pd.Series(Y_pred).map({"not spam":0,"spam":1})

X_plot=X_test.toarray()
plt.subplot(1,2,1)
plt.scatter(X_plot[:,0],X_plot[:,1],c=actual)
plt.title("Actual")

plt.subplot(1,2,2)
plt.scatter(X_plot[:,0],X_plot[:,1],c=predicted)
plt.title("Predicted")

plt.tight_layout()
plt.show()
