#1.  trout per year (bar chart)
#2. % in cities (pie)
#3. Total amount of eggs hatched per year (Line chart)

import matplotlib.pyplot as plt
import numpy as np
 
year=['2014', '2015', '2016', '2017', '2018']
pos = np.arange(len(year))
eggs=[150,190,160,110,230]
 
plt.bar(pos,eggs,color='lime',edgecolor='#333')
plt.xticks(pos, year)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Eggs Hatched', fontsize=16)
plt.title('Number of Trout Eggs Hatched',fontsize=20)
plt.show()