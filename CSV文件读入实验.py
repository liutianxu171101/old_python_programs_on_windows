import csv
import numpy as np
from matplotlib import pyplot as plt

data = []
f = open('房价+坐标.csv','r',newline='',encoding='UTF-8')
csv_reader = csv.reader(f)
for row in csv_reader:
    if (row[2]=='价格'):
        continue
    else:
        data.append(int(row[2]))
f.close()

x = np.linspace(0,1000,51)
plt.hist(data,x,rwidth=0.9)
plt.grid(axis='y',alpha=0.7)
plt.show()
