"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 19-OCT-2023
"""

from datetime import datetime

current_dateTime = datetime.now()
print('\n\nRun Date is ', current_dateTime)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([2,3,4,5,6,7,8,9,10,11]).reshape((-1, 1))
y = np.array([30,25,95,115,265,325,570,700,1085,1300])

model = LinearRegression()
model.fit(x, y)

r_sq = model.score(x, y)
print("\nCoefficient of linear correlation: ", r_sq)
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)

y_pred = model.intercept_ + model.coef_ * x
print("Values of b1, b0 : \n", y_pred)

x_new = np.linspace(0, 20, 50)
y_new = model.predict(x_new[:, np.newaxis])

plt.figure(figsize=(4, 3))
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new)

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.axis('tight')

plt.show()