"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 27-Nov-2023
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)

import numpy as np
import math

n_good = 9
n_defective = 3

n_total = n_good + n_defective
k = 3
p_X = np.zeros(k + 1)

for x in range(k + 1):
    C_nk = math.factorial(n_total) / (math.factorial(x) * math.factorial(n_total - x))
    p_X[x] = C_nk * ((n_good / n_total) ** x) * ((n_defective / n_total) ** (n_total - x))

print("Probability distribution of X:",p_X)

mean_X = np.sum(p_X * np.arange(k + 1))
variance_X = np.sum(p_X * (np.arange(k + 1) - mean_X) ** 2)

print("Mean of X:", mean_X)
print("Variance of X:", variance_X)

p_accept = p_X[k]
print("Probability that the entire batch of TV sets can be accepted:", p_accept)