"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 19-OCT-2023
"""

from datetime import datetime

current_dateTime = datetime.now()
print('\n\nRun Date is ', current_dateTime)

import matplotlib.pyplot as plt
import pandas as pd
import math

def calc_mean(list):
  sum = 0
  for number in list:
    sum += number
  return sum / len(list)


def calc_var(list):
    mean = calc_mean(list)
    summed = 0
    for x in list:
        summed += (x - mean)**2
    return summed / (len(list))

def calc_median(list):
    indices = []
    list_size = len(list)
    median = 0
    if list_size % 2 == 0:
        indices.append(int(list_size / 2) - 1)  # -1 because index starts from 0
        indices.append(int(list_size / 2))
        median = (list[indices[0]] + list[indices[1]]) / 2
    else:
        indices.append(int(list_size / 2))
        median = list[indices[0]]
    return median, indices


def calc_std(list):
  mn=0
  mn= calc_mean(list)
  variance = 0
  for number in list:
    variance += (number - mn) ** 2
  variance /= len(list) - 1
  return variance ** 0.5

def calc_Q(data, percentile):
    n = len(data)
    p = n * percentile / 100
    if p.is_integer():
        return sorted(data)[int(p)]
    else:
        return sorted(data)[int(math.ceil(p)) - 1]

def calc_zscore(list):
    mean = calc_mean(list)
    std = calc_std(list)
    zscores = [(s - mean) / std for s in list]
    return zscores

file_name = "C:\\1Mahesh Hemework\\Math208\\original_diabetes.xlsx"
sheet="diabetes"
df = pd.read_excel(io=file_name, sheet_name=sheet, nrows=31)

print("\nGlucose Mean: ",calc_mean(df["Glucose"]))
print("Glucose Median: ",calc_median(df["Glucose"]))
print("Glucose Var: ",calc_var(df["Glucose"]))
print("Glucose STD : ",calc_std(df["Glucose"]))
print("Glucose Q1  : ",calc_Q(df["Glucose"],25))
print("Glucose Q3  : ",calc_Q(df["Glucose"],75))
print("Glucose Zscore  : ",calc_zscore(df["Glucose"]))

print("\nBlood Pressure Mean: ",calc_mean(df["BloodPressure"]))
print("Blood Pressure Median : ",calc_median(df["BloodPressure"]))
print("Blood Pressure Var : ",calc_var(df["BloodPressure"]))
print("Blood Pressure STD : ",calc_std(df["BloodPressure"]))
print("Blood Pressure Q1  : ",calc_Q(df["BloodPressure"],25))
print("Blood Pressure Q3  : ",calc_Q(df["BloodPressure"],75))
print("Blood Pressure Zscore : ",calc_zscore(df["BloodPressure"]))

# Creating plot
data=[df["Glucose"], df["BloodPressure"]]

plt.boxplot(data)

# show plot
plt.show()


