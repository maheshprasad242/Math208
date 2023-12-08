"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 7-Dec-2023
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)

import numpy as np

n_values = range(51, 101)
p = 0.05

means = []
std_devs = []

for n in n_values:
    mean = n * p
    std_dev = np.sqrt(n * p * (1 - p))
    means.append(mean)
    std_devs.append(std_dev)


print("n\tMean\tStandard Deviation")
for i, n in enumerate(n_values):
    print(f"{n}\t{means[i]:.3f}\t{std_devs[i]:.3f}")
