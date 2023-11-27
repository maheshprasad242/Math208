"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 27-Nov-2023
Description : Convert number from any base to any base
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)

pA = 10**(-4)
pBA = 1-(10**(-6))
pBiA = 1/10

print('Probability of luggage containing prohibited items is ',pA)
print('Probability of falsely identifying a regular luggage as containing prohibited items is ',pBiA)
print('Probability of falsely identifying prohibited items as regular luggage is  ',pBA)

pResult = (pBA * pA)/(pBA * pA + pBiA * (1 - pA))

print ('\nProbability to contain prohibited items is ',pResult)
