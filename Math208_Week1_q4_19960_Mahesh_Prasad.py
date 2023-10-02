"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 01-OCT-2023
"""

from datetime import datetime

current_dateTime = datetime.now()
print('\n\nRun Date is ', current_dateTime)

import math

def calc_median(sorted_list):

    indices = []

    list_size = len(sorted_list)
    median = 0

    if list_size % 2 == 0:
        indices.append(int(list_size / 2) - 1)  # -1 because index starts from 0
        indices.append(int(list_size / 2))

        median = (sorted_list[indices[0]] + sorted_list[indices[1]]) / 2
        pass
    else:
        indices.append(int(list_size / 2))

        median = sorted_list[indices[0]]
        pass

    return median, indices
    pass


def prect(data, percentile):
    n = len(data)
    p = n * percentile / 100
    if p.is_integer():
        return sorted(data)[int(p)]
    else:
        return sorted(data)[int(math.ceil(p)) - 1]


offender_list = [11,14,15,15,16,16,17,18,19,21,25,36,
                 12,14,15,15,16,16,17,18,19,21,25,39,
                 13,14,15,15,16,17,17,18,20,22,26,43,
                 13,14,15,15,16,17,17,18,20,22,26,46,
                 13,14,15,16,16,17,17,18,20,22,27,50,
                 13,14,15,16,16,17,17,19,20,23,27,54,
                 13,14,15,16,16,17,18,19,20,23,29,59,
                 13,15,15,16,16,17,18,19,20,23,30,67,
                 14 ,15,15,16,16,17,18,19,21,24,31,
                 14,15,15,16,16,17,18,19,21,24,34]

print('\nData is')
print(offender_list)

uniq_values = []
mode_values = []
for i in offender_list:
    if i not in uniq_values:
        uniq_values.append(i)
    else:
        mode_values.append(i)

print('\nMode is ',set(mode_values))

offender_list.sort()
median, median_indices = calc_median(offender_list)
Q1, Q1_indices = calc_median(offender_list[:median_indices[0]])
Q3, Q3_indices = calc_median(offender_list[median_indices[-1] + 1:])

print('\nMedian is ',median)

print('\nQ1 is ',Q1)
print('Q3 is',Q3)

print('\nP10 is ',prect(offender_list, 10))
print('P95 is ',  prect(offender_list, 95))