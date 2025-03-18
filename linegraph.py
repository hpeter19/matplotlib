import numpy as np
import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]
weight =[ 12,12,15,13,16,16,18,16,11,11,16,18,19,23,24,15]
#line graph

plt.plot(years,weight, c="g",lw=4)
plt.show()
#print(years)

