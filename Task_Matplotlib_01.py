# -*- coding: utf-8 -*-
"""Copy of task-23.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y0KtNuSSGL-4Mu2ajClga-BPPYwQ-kYp
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

plt.style.use('default')

"""## `Problem 1 to 5`:

Dataset link: https://tinyurl.com/2fe6vz4u

**Add a label to every axis and add a proper title for the charts. Also add proper labels if there are multiple representations.** Then, you can customize it as your wish.

### **`Problem-1:`** Draw a line plot of which, the x-axis is the "Year" and the y-axis is sum of "PM2.5" of two countries Iran and China.
"""

df = pd.read_csv('https://tinyurl.com/2fe6vz4u')
df

ir = df[df['Country']=='Iran'].groupby(['Country','Year'])['PM2.5'].sum().reset_index()
ch = df[df['Country']=='China'].groupby(['Country','Year'])['PM2.5'].sum().reset_index()

plt.plot(ir['Year'], ir['PM2.5'], label='Iran')
plt.plot(ch['Year'], ch['PM2.5'], label='China')
plt.xlabel('Year')
plt.ylabel('PM2.5')
plt.title('China and Irans PM2.5 over years')
plt.legend()

"""### **`Problem-2:`** Draw a histogram of the  column "PM10" of which the y-axis represents the probability (see the documentation how to draw the probability)."""

plt.hist(df['PM10'], bins=50, density=True)
plt.xlabel('PM10')
plt.ylabel('Probability')
plt.title('PM10 vs Probability')
plt.show()

"""### **`Problem-3:`** Draw a scatter plot where x-axis represents "PM2.5" and y-axis represents "PM10" for two countries Poland and Chile."""

plnd = df[df['Country']=='Poland']
chl = df[df['Country']=='Chile']

plt.scatter(plnd['PM2.5'], plnd['PM10'], label='Poland')
plt.scatter(chl['PM2.5'], chl['PM10'], label='Chile')
plt.xlabel('PM2.5')
plt.ylabel('PM10')
plt.legend()

"""### **`Problem-4:`** Draw a pie chart of top 5 most frequent countries."""

plt.pie(df['Country'].value_counts().head(), labels=df['Country'].value_counts().head().index, autopct='%0.1f%%',explode=[0,0,0.1,0,0])
plt.show()

"""### **`Problem-5:`** Draw a bar chart which represents the counts of top 5 most frequent countries.


"""

x = df['Country'].value_counts().head().index
y = df['Country'].value_counts().head().values
plt.bar(x,y)

"""##`Problem 6-10`
Data Set - https://docs.google.com/spreadsheets/d/e/2PACX-1vTJh6X4_mqixWsfK9mgkllGQkKYW9Wj9kOIMGY2uYsWeS8n5np87DO-SDGQWJ1HXEnxiOVFVzYFYEcR/pub?gid=558678488&single=true&output=csv

This is a Sales data of any company in a Year.


###`Problem-6`
Show a line plot of Total Profit for each month with below styling.
* Dotted Line
* Line Color Blue
* Show Legend at top left
* Circle Marker
"""

# code here
df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTJh6X4_mqixWsfK9mgkllGQkKYW9Wj9kOIMGY2uYsWeS8n5np87DO-SDGQWJ1HXEnxiOVFVzYFYEcR/pub?gid=558678488&single=true&output=csv')

plt.plot(df['month_number'],df['total_profit'], linestyle='dotted', color='Blue', label='Total Profit', marker='.')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.legend()

"""###`Problem-7`
Show sales of each product in march month as pie chart.
* Show Percentage value
* Give Title "Sales in March"
* Explode ToothPaste with shadow
"""

sales = df[df['month_number']==3].stack().droplevel(0).drop(labels=['month_number','total_units','total_profit'])
plt.pie(sales.values, labels=sales.index, autopct='%0.1f%%', shadow=True, explode=[0,0,0.1,0,0,0])
plt.title('Sales in March')
plt.show()

"""###`Problem-8` Multiline Plot of all products sales.
* Give different styes for each products
* Add legend at top right
"""

plt.plot(df['month_number'], df['facecream'], label='facecream')
plt.plot(df['month_number'], df['facewash'], linestyle='dashed', label='facewash')
plt.plot(df['month_number'], df['toothpaste'], linestyle='dotted', label='toothpaste')
plt.plot(df['month_number'], df['bathingsoap'], linestyle='--', label='bathingsoap')
plt.plot(df['month_number'], df['shampoo'], linestyle='-.', label='shampoo')
plt.plot(df['month_number'], df['moisturizer'],linestyle=':', label='moisturizer')

plt.xticks(df['month_number'])
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper right')

"""###`Problem-9` Show Quarter wise Sales data for all products as multi Bar chart.

"""

df.columns

df['date'] = pd.to_datetime([f'2024-{i}-1' for i in df['month_number']])
df['quarter'] = df['date'].dt.quarter
data = df.groupby('quarter')[['facecream', 'facewash', 'toothpaste', 'bathingsoap',
       'shampoo', 'moisturizer']].sum()
data

a = -1
for i in data.columns:
  plt.bar([b+a for b in data.index], data[i], width= 0.15, label=i)
  a = a - 0.15

plt.xticks(data.index-1.2, data.index)
plt.legend()
plt.xlabel('Products per Quarter')
plt.ylabel('Sales')
plt.show()

"""###`Problem-10` Plot Stacked Bar chart quarter wise for each product."""

