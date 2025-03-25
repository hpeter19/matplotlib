import numpy as np
import matplotlib.pyplot as plt

import random

ax =plt.axes(projection="3d")

x =np.arange(0,50,0.1)
y =np.arange(0,50,0.1)
z=np.cos(x+y)

ax.plot(x, y, z)
ax.set_title("3d Plot")
ax.set_xlabel("Test")
plt.show()