"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 01-OCT-2023
"""
import random

def generate_random_numbers(n, min_value, max_value):
  random_numbers = []
  for i in range(n):
    random_numbers.append(random.uniform(min_value, max_value))
  return random_numbers


def calc_mean(numbers):
  mean = sum(numbers) / len(numbers)
  return mean

def calc_median(numbers):
  numbers.sort()
  median = numbers[len(numbers) // 2]
  return median

def calc_standard_deviation(numbers):
  mean = calc_mean(numbers)
  variance = sum([(number - mean)**2 for number in numbers]) / len(numbers)
  standard_deviation = variance**0.5
  return standard_deviation

random_numbers = generate_random_numbers(500, -20, 20)

print(random_numbers)

mean = calc_mean(random_numbers)
median = calc_median(random_numbers)
standard_deviation = calc_standard_deviation(random_numbers)

print("Mean:", mean)
print("Median:", median)
print("Standard deviation:", standard_deviation)