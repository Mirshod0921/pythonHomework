import numpy as np
import matplotlib.pyplot as plt


time_periods = ['T1', 'T2', 'T3', 'T4']
categories = ['Category A', 'Category B', 'Category C']


data = np.array([
    [10, 20, 30, 40],  
    [22, 33, 28, 23],  
    [31, 20, 40, 10]   
])

bar_width = 0.6

fig, ax = plt.subplots(figsize=(8, 6))

bottom = np.zeros(len(time_periods))  
colors = ['r', 'g', 'b']  

for i, category in enumerate(categories):
    ax.bar(time_periods, data[i], bottom=bottom, label=category, color=colors[i])
    bottom += data[i] 


ax.set_xlabel('Time Periods')
ax.set_ylabel('Value')
ax.set_title('Stacked Bar Chart of Categories Over Time')
ax.legend(title='Categories')

plt.show()