import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

data=pd.read_csv("multiple.csv")

X=data[["area","bedroom","years"]]
Y=data[["price"]]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=11)

model=linear_model.LinearRegression()
model.fit(X_train,Y_train)

y_pred=model.predict(X_test)

print("Mean Squared error:",round(mean_squared_error(Y_test,y_pred),2))
print("R2 Score:",round(r2_score(Y_test,y_pred),2))
print("Coeffiecients:",round(model.coef_[0][0],2))
print("Intercept:",round(model.intercept_[0],2))

sample=pd.DataFrame([[470,3,1]],columns=["area","bedroom","years"])
result=model.predict(sample)

print("House price:",result[0][0])

plt.scatter(X["area"],Y["price"],c="green",marker="*",label="Actual")
plt.plot(X_test["area"],model.predict(X_test),c="red",linewidth=3,label="predicted")

plt.title("Multiple Regression")
plt.xlabel("area")
plt.ylabel("price")
plt.legend()
plt.show()