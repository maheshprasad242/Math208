"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 27-Nov-2023
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)

import numpy as np

def calculate_probability(k):
    p_values = np.array([0.2, 0.1 * (k + 1), 0.3 * (k + 1), 0.2])
    return p_values

x_values = np.array([0, 1, 2, 3])

expected_values = []
for k in x_values:
    p_values = calculate_probability(k)
    expected_value = np.dot(x_values, p_values)
    expected_values.append(expected_value)

print("Expected values for different values of X:")
for X, expected_value in zip(x_values, expected_values):
    print("X =", X, ", E(X) =", expected_value)





