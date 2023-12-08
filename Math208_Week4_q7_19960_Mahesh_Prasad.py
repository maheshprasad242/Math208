"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 7-Dec-2023
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

random_numbers = stats.t.rvs(df=10, size=100)

mean = np.mean(random_numbers)
std_dev = np.std(random_numbers)

sampling_groups = []
for _ in range(15):
    sample = np.random.choice(random_numbers, size=30)
    sampling_groups.append(sample)

sampling_group_means = [np.mean(group) for group in sampling_groups]

overall_mean = np.mean(sampling_group_means)

std_err = std_dev / np.sqrt(len(sampling_groups))

print("Mean of 100 random numbers:", mean)
print("Standard deviation of 100 random numbers:", std_dev)
print("Mean of sampling group means:", overall_mean)
print("Standard error of the mean:", std_err)

plt.hist(sampling_group_means, bins=20)
plt.xlabel("Mean of sampling group")
plt.ylabel("Frequency")
plt.title("Histogram of sampling group means")
plt.show()

