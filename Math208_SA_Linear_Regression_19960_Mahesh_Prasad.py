"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 16-DEC-2023
"""

from datetime import datetime

current_dateTime = datetime.now()
print('\n\nLinear Regression Run Date is ', current_dateTime)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression


data = pd.read_csv ('C:\\1Mahesh Hemework\\Math208\\Cardiovascular_Disease_Dataset.csv')
print(data.head())

x=data[['age','gender']].values
y=data['maxheartrate'].values


model = LinearRegression()
model.fit(x, y)

r_sq = model.score(x, y)
print("\nCoefficient of linear correlation r : ", r_sq)
print("Intercept b0: ", model.intercept_)
print("Slope bi: ", model.coef_)

