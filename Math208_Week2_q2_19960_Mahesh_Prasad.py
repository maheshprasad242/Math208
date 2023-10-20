"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 19-OCT-2023
"""

from datetime import datetime

current_dateTime = datetime.now()
print('\n\nRun Date is ', current_dateTime)


import random

def generate_random_range(n, min_value, max_value):
  rn = []
  for i in range(n):
    rn.append(random.uniform(min_value, max_value))
  return rn


def generate_random_var(n, mean, std):
  rn = []
  for i in range(n):
    rn.append(random.normalvariate(mean, std))
  return rn

def calc_mean(list):
  sum = 0
  for number in list:
    sum += number
  return sum / len(list)

def calc_std(list):
  mn=0
  mn= calc_mean(list)
  variance = 0
  for number in list:
    variance += (number - mn) ** 2
  variance /= len(list) - 1
  return variance ** 0.5

def verify_Chebyshev_ineq(list, k):
  mean = calc_mean(list)
  std  = calc_std(list)
  listcount = len(list)
  counter = 0
  for number in list:
      if mean - (k*std) <= number <= mean + (k*std):
        counter += 1

  Probability = counter/listcount
  Result = counter/listcount >= 1-1/(k**2)
  print("When k = ", k, "Probability = :", Probability, " >= ", 1-1/(k**2) , " is " , Result  )
  return

random_var = generate_random_var(50, 10, 0.5)
print("\nNormal Distribution : ", random_var)

verify_Chebyshev_ineq(random_var, 1)
verify_Chebyshev_ineq(random_var, 2**0.5)
verify_Chebyshev_ineq(random_var,1.5)
verify_Chebyshev_ineq(random_var, 2)
verify_Chebyshev_ineq(random_var, 3)


random_range = generate_random_range(50, -20, 20)
print("\nRange [-20,+20] : ", random_range)

verify_Chebyshev_ineq(random_range, 1)
verify_Chebyshev_ineq(random_range, 2**0.5)
verify_Chebyshev_ineq(random_range,1.5)
verify_Chebyshev_ineq(random_range, 2)
verify_Chebyshev_ineq(random_range, 3)