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

n_male = 30
n_female = 20

n_total = n_male + n_female
k = 5

p_X = np.zeros(k + 1)

for x in range(k + 1):
    C_nk = math.factorial(n_total) / (math.factorial(x) * math.factorial(n_total - x))
    p_X[x] = C_nk * ((n_female / n_total) ** x) * ((n_male / n_total) ** (n_total - x))

print("Probability distribution of X:", p_X)

