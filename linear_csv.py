import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
# from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split

data=pd.read_csv("lineardatacsv.csv")

X=data[["years"]]
y=data[["salary"]]

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.30,random_state=78)
# scalar=StandardScaler()
# X_train=scalar.fit_transform(X_train)
# X_test=scalar.transform(X_test)

model=linear_model.LinearRegression()
model.fit(X_train,Y_train)

Y_pred=model.predict(X_test)

print("Mean Squared Error:",mean_squared_error(Y_test,Y_pred))
print("R^2 Score:",r2_score(Y_test,Y_pred))
print("coefficients:",model.coef_)
print("Intercepts:",model.intercept_)

sample=pd.DataFrame([[11]],columns=["years"])
# sample_scaled=scalar.transform(sample)
result=model.predict(sample)
print("Salary is :",result[0])

plt.scatter(X["years"],y["salary"],c="black")
plt.plot(X_test["years"],Y_pred,c="blue",linewidth=3)
plt.show()