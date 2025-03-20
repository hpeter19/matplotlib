from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#setting dark background
style.use("dark_background")
votes=[13,10,26,33,40]
people=["A","B","C","D","E"]

plt.pie(votes,labels=None)
plt.legend(labels =people)
plt.show()