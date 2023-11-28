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

defective_tv = 3
good_tv = 12 - defective_tv

n = 3
probability = np.zeros(n + 1)

def calculate_probability(k):
    binomial_coefficient = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    defective_probability = (defective_tv / good_tv) ** k
    good_probability = (good_tv / (good_tv + defective_tv)) ** (n - k)
    return binomial_coefficient * defective_probability * good_probability

for k in range(0, n + 1):
    probability[k] = calculate_probability(k)

probability_third_defective = probability[1]
print('Probability that the third one is one defective:',probability_third_defective)
