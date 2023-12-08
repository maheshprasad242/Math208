"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 7-Dec-2023
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)

import scipy.stats as stats

mean = 10.3
std_dev = 0.65

p_less_than_9 = stats.norm.cdf(9, mean, std_dev) * 100
print("Percentage of anchovies less than 9cm:", p_less_than_9, "%")

p_between_9_5_and_10_6 = (stats.norm.cdf(10.6, mean, std_dev) - stats.norm.cdf(9.5, mean, std_dev)) * 100
print("Percentage of anchovies between 9.5cm and 10.6cm:", p_between_9_5_and_10_6, "%")

z_score = stats.norm.ppf(0.8, loc=mean, scale=std_dev)

minimum_length = mean + z_score * std_dev
print("Minimum length for the top 20% of anchovies:", minimum_length, "cm")

