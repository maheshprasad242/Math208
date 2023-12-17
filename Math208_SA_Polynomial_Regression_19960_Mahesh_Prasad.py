"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 16-DEC-2023
"""

from datetime import datetime

current_dateTime = datetime.now()
print('Polynomial Regression Run Date is ', current_dateTime)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression
from   sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv ('C:\\1Mahesh Hemework\\Math208\\Cardiovascular_Disease_Dataset.csv')

x=data['age'].values
y=data['maxheartrate'].values

x=x.reshape((-1, 1))

print('Include_bias=False')
transformer = PolynomialFeatures(degree=2, include_bias=False)
transformer.fit(x)
x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)

model = LinearRegression()
model.fit(x_, y)

r_sq = model.score(x_, y)
print("Coefficient of determination : ", r_sq)
print("Intercept: ", model.intercept_)
print("Slope : ", model.coef_)

print('Include_bias=True')
x_ = PolynomialFeatures(degree=2, include_bias=True).fit_transform(x)
model = LinearRegression(fit_intercept=False).fit(x_, y)
r_sq = model.score(x_, y)

print("Coefficient of determination : ", r_sq)
print("Intercept: ", model.intercept_)
print("Slope : ", model.coef_)

print("Advanced Linear Regression")
import statsmodels.api as sm
model = sm.OLS(y, x_)
results = model.fit()
print(results.summary())