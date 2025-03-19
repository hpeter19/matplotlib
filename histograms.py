#using random values generate by numpy

import numpy as np
import matplotlib.pyplot as plt

ages=np.random.normal(20,1.5,100)
plt.hist(ages)
plt.show()

