import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

import random

ax =plt.axes(projection="3d")

x =np.arange(-5,5,0.1)
y =np.arange(-5,5,0.1)

X,Y =np.meshgrid(x,y)


Z=np.sin(X)* np.cos(Y)

#adding some colors using spectral function
ax.plot_surface(X,Y,Z , cmap="Spectral")
ax.set_title("3d Plot")
ax.set_xlabel("Test")

plt.show()


plt.savefig("Scatterplot.png")