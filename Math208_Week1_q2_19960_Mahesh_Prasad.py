"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 01-OCT-2023
"""
from datetime import datetime

current_dateTime = datetime.now()
print('\n\nRun Date is ', current_dateTime)



import random
import matplotlib.pyplot as plt

def generate_random_numbers(n, min_value, max_value):

  rn = []
  for i in range(n):
    rn.append(random.normalvariate(10, 0.5))
  return rn


def mean(list_of_numbers):
  sum = 0
  for number in list_of_numbers:
    sum += number
  return sum / len(list_of_numbers)


def median(list_of_numbers):
  list_of_numbers.sort()
  if len(list_of_numbers) % 2 == 1:
    return list_of_numbers[len(list_of_numbers) // 2]
  else:
    return (list_of_numbers[len(list_of_numbers) // 2] + list_of_numbers[len(list_of_numbers) // 2 - 1]) / 2


def standard_deviation(list_of_numbers):
  mn=0
  mn= mean(list_of_numbers)
  variance = 0
  for number in list_of_numbers:
    variance += (number - mn) ** 2
  variance /= len(list_of_numbers) - 1
  return variance ** 0.5


for i in range(500):
  random_numbers = generate_random_numbers(500, -20, 20)

mn = 0
mn = mean(random_numbers)
md=0
md = median(random_numbers)
sd=0
sd = standard_deviation(random_numbers)

print("Mean:", mn)
print("Median:", md)
print("Standard deviation:", sd)


plt.hist(random_numbers, bins=10)
plt.xlabel("Random number")
plt.ylabel("Frequency")
plt.title("Histogram of 500 random numbers from a Gaussian distribution with mean 10 and standard deviation 0.5")
plt.show()