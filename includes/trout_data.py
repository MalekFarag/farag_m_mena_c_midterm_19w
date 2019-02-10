#1. trout per year (bar chart)
#2. fish caught per year in each creek (bar chart)
#3. Total amount of eggs hatched per year (Line chart)

import matplotlib.pyplot as plt
import numpy as np
 
#1. number of eggs hatched per year
year=['2014', '2015', '2016', '2017', '2018']
pos = np.arange(len(year))
eggs=[150,190,160,110,230]
 
plt.bar(pos,eggs,color='lime',edgecolor='#333')
plt.xticks(pos, year)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Eggs Hatched', fontsize=16)
plt.title('Number of Trout Eggs Hatched',fontsize=20)
plt.show()


#2. fish caught per year in each creek
n_groups = 3
Komoka = (15, 14, 23)
Oxbow = (10, 18, 14)
Dingman = (13, 15, 14)

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, Komoka, bar_width,
alpha=opacity,
color='b',
label='Komoka')
 
rects2 = plt.bar(index + bar_width, Oxbow, bar_width,
alpha=opacity,
color='g',
label='Oxbow')

rects3 = plt.bar(index + bar_width, Dingman, bar_width,
alpha=opacity,
color='y',
label='Dingman')
 
plt.xlabel('Year')
plt.ylabel('Fish Caught')
plt.title('Fish Caught in Different Creek (per year)')
plt.xticks(index + bar_width, ('2016', '2017', '2018'))
plt.legend()
 
plt.tight_layout()
plt.show()



#3. Total Amount of Eggs Hatched (brown + rainbow)
rainbow = [100, 150, 100, 50, 150]
brown = [100, 80, 70, 80, 100]
plt.plot(year, rainbow, color='g')
plt.plot(year, brown, color='orange')
plt.xlabel('Year')
plt.ylabel('Total Eggs Hatched by the Thousands')
plt.title('Rainbow and Brown Trout Eggs Hatched')
plt.show()