from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

import numpy as np
import math

fig = plt.figure()
axes3d = Axes3D(fig)
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
x,y = np.meshgrid(x,y)
z = x**2-y**2
image = axes3d.plot_surface(x,y,z,cmap = 'autumn')

plt.show()
