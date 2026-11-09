from sklearn.datasets import load_diabetes
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
import matplotlib.pyplot as plt

diabetes_X,diabetes_y=load_diabetes(return_X_y=True)
diabetes_X=diabetes_X[:,np.newaxis,2]
diabetes_X_train=diabetes_X[:-20]
diabetes_X_test=diabetes_X[-20:]
diabetes_y_train=diabetes_y[:-20]
diabetes_y_test=diabetes_y[-20:]

regr_model=linear_model.LinearRegression()
regr_model.fit(diabetes_X_train,diabetes_y_train)
y_pred=regr_model.predict(diabetes_X_test)
print("Coefficients: ",regr_model.coef_)
print("Intercept: ",regr_model.intercept_)
print("Mean squared Error:",mean_squared_error(diabetes_y_test,y_pred))
print("R^2 Score:",r2_score(diabetes_y_test,y_pred))

plt.scatter(diabetes_X_test,diabetes_y_test,c="black")
plt.plot(diabetes_X_test,y_pred,color="blue",linewidth=3)

plt.xlabel("BMI")
plt.ylabel("Diabets Progression")
plt.title("Diabetes Progression Regression graph")
plt.show()