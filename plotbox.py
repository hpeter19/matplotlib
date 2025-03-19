import numpy as np
import matplotlib.pyplot as plt

heights =np.random.normal(172,10,200)
plt.boxplot(heights)
plt.show()
#used to show mean,standard variation and variation