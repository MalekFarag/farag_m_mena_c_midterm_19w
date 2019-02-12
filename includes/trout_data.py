#1. trout per year (bar chart)
#2. fish caught per year in each creek (bar chart)
#3. Total amount of eggs hatched per year (Line chart)

import matplotlib.pyplot as plt
import numpy as np
 
#1. number of eggs hatched per year
year=['2014', '2015', '2016', '2017', '2018']
pos = np.arange(len(year))
eggs=[150,190,160,110,230]
 
plt.bar(pos,eggs,color='green',edgecolor='black')
plt.xticks(pos, year)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Eggs Hatched', fontsize=16)
plt.title('Number of Trout Eggs Hatched',fontsize=20)
plt.show()


#2. fish caught in each creek
labels = 'Komoka', 'Oxbow', 'Dingman'
sizes = [52, 42, 42]
colors = ['gold', 'yellowgreen','lightskyblue']
explode = (0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
/Users/m_farag/Downloads/farag_m_mena_c_midterm_19w-dev.faragm.anglers1/trout.html
plt.axis('equal')
plt.title('Fish Caught in Each Creek',fontsize=18)
plt.show()

#3. Total Amount of Eggs Hatched (brown + rainbow)
rainbow = [100, 250, 350,400, 550]
brown = [100, 180, 250, 330, 430]
plt.plot(year, rainbow, color='green')
plt.plot(year, brown, color='orange')
plt.xlabel('Year')
plt.ylabel('Eggs Hatched by the Thousands')
plt.legend(['Rainbow Trout', 'Brown Trout'])
plt.title('Total Rainbow and Brown Trout Eggs Hatched Through the Years')
plt.show()
