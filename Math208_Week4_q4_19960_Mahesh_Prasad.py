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
import math
import scipy.stats as stats

n = 100
p = 0.2

exact_probabilities = np.zeros(n + 1)
for k in range(0, n + 1):
    exact_probabilities[k] = math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) * (p ** k) * ((1 - p) ** (n - k))

mu = n * p
sigma = np.sqrt(n * p * (1 - p))
normal_probabilities = []
for k in range(0, n + 1):
    normal_probabilities.append(stats.norm.cdf(k + 0.5, mu, sigma) - stats.norm.cdf(k - 0.5, mu, sigma))

print(exact_probabilities)
print(normal_probabilities)

plt.figure(figsize=(10, 6))
plt.hist(exact_probabilities, bins=n + 1, label='Exact Binomial', edgecolor='black', alpha=0.7)
plt.hist(normal_probabilities, bins=n + 1, label='Normal Approximation', edgecolor='black', alpha=0.7)
plt.xlabel('Number of successes (k)')
plt.ylabel('Probability')
plt.title('Comparison of Exact Binomial and Normal Approximation Probabilities')
plt.legend()
plt.grid(True)
plt.show()