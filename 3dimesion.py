import numpy as np
import matplotlib.pyplot as plt

import random

ax =plt.axes(projection="3d")

x =np.random.random(100)
y =np.random.random(100)
z=np.random.random(100)

ax.scatter(x, y, z)
ax.set_title("3d Plot")
plt.show()