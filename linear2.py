import matplotlib.pyplot as plt
import pandas as pd

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

data=pd.read_csv("house.csv")
X=data[["area"]]
Y=data[["price"]]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=11)
model=linear_model.LinearRegression()
model.fit(X_train,Y_train)
y_pred=model.predict(X_test)

print("Mean Squared Error:",round(mean_squared_error(Y_test,y_pred),2))
print("R2 Score:",round(r2_score(Y_test,y_pred),2))
print("Coefficients:",model.coef_[0][0])
print("intercept:",model.intercept_[0])

sample=pd.DataFrame([[1800]],columns=["area"])
result=model.predict(sample)

print("The house price is:",result[0][0])

plt.scatter(X["area"],Y["price"],c="black")
plt.plot(X_test["area"],y_pred,c="red",linewidth=3)
plt.title("Regression")
plt.xlabel("Area(sqft)")
plt.ylabel("Price")
plt.show()