from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
#Adding information to the plot
stock_a=[100,120,130,115,100,123,104,111]
stock_b=[88,95,78,81,99,89,100,106,109]
stock_c=[55,49,77,88,99,104,109,114,118]

plt.plot(stock_a , label="Company 1")
plt.plot(stock_b,label="Company2")
plt.plot(stock_c,label="Company 3")
plt.legend()

plt.show()