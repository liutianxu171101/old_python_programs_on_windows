from matplotlib import pyplot as plt
import numpy as np
import math

x = np.linspace(0,2*math.pi,21)
y1,y2 = np.sin(x),np.cos(x)

plt.subplot2grid((1,2),(0,0),colspan = 1)
plt.plot(x,y1)

plt.subplot2grid((1,2),(0,1),colspan = 1)
plt.plot(x,y2)

plt.show()

