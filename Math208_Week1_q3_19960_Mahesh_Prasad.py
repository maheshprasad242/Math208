"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 01-OCT-2023
"""
from datetime import datetime

current_dateTime = datetime.now()
print('\n\nRun Date is ', current_dateTime)

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.DataFrame({'Number X 10,000': [7.2, 12.5, 7.2, 63.2, 5.6, 56.0, 12.2, 4.5, 3.4, 13.7 ]})
df.index = ['Alzheimers', 'Chronic Respiratory Disease', 'Diabetes', 'Heart Disease', 'Influenza/Pneumonia', 'Malignant Neoplasms','Accidents','Nephritis/Nephrosis','Septicemia','Stroke']


df = df.sort_values(by='Number X 10,000', ascending=False)

df['cumperc'] = df['Number X 10,000'].cumsum()/df['Number X 10,000'].sum()*100

print(df)

color1 = 'steelblue'
color2 = 'red'
line_size = 4

fig, ax = plt.subplots()
ax.bar(df.index, df['Number X 10,000'], color=color1)

ax2 = ax.twinx()
ax2.plot(df.index, df['cumperc'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)

plt.show()