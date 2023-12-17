"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 16-DEC-2023
"""

from datetime import datetime

current_dateTime = datetime.now()
print('\n\nSimple Regression Run Date is ', current_dateTime)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression


data = pd.read_csv ('C:\\1Mahesh Hemework\\Math208\\Cardiovascular_Disease_Dataset.csv')
print(data.head())

x=data['age'].values
y=data['maxheartrate'].values

x=x.reshape((-1, 1))

model = LinearRegression()
model.fit(x, y)

r_sq = model.score(x, y)
print("\nCoefficient of linear correlation r : ", r_sq)
print("Intercept b: ", model.intercept_)
print("Slope m: ", model.coef_)

x_new = np.linspace(0, 100, 1000)
y_new = model.predict(x_new[:, np.newaxis])

plt.figure(figsize=(4, 3))
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new)

ax.set_xlabel('Age')
ax.set_ylabel('MaxHeartRate')

ax.axis('Tight')

plt.show()