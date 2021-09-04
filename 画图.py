import numpy as np
from matplotlib import pyplot as plt
import math

x = np.linspace(0,3*math.pi,200)
y1,y2 = np.sin(x),np.cos(x)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False       #解决负数坐标显示问题

plt.figure
plt.plot(x,y1,color='red', linewidth=1.5,linestyle='-',label=r'$sin(t)$')
plt.plot(x,y2,color='blue',linewidth=1.5,linestyle='-',label=r'$cos(t)$')
plt.title('插森')
plt.xlabel('森哥凉了')
plt.ylabel('森哥挂了')
plt.legend(loc = 'best',frameon = False)
plt.grid()
plt.show()
