import numpy as np
import matplotlib.pyplot as plt

ages=np.random.normal(20,1.5,100)
plt.hist(ages, bins=10, cumulative=True)
#comulative histograms
plt.show()

