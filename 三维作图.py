from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

import numpy as np
import math

fig = plt.figure()
axes3d = Axes3D(fig)

'''plt.subplot2grid((1,3),(0,0),colspan = 1)
#散点图
x = np.random.random((1,100))
y = np.random.random((1,100))
z = np.random.random((1,100))
axes3d.scatter(x,y,z)

plt.subplot2grid((1,3),(0,1),colspan = 1)
x = np.linspace(0,20,100)
y = np.sin(x)
z = np.cos(x)
axes3d.plot(x,y,z)

plt.subplot2grid((1,3),(0,2),colspan = 1)'''

x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
x,y = np.meshgrid(x,y)
z = x**2-y**2
image = axes3d.plot_surface(x,y,z,cmap = 'autumn')

plt.show()
