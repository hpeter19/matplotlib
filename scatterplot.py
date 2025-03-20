#generating a scatter plot with random data using matplotlib
import numpy as np
import matplotlib.pyplot as plt



x_data= np.random.random(50)*100
y_data = np.random.random(50) * 100
plt.scatter(x_data,y_data,c="red",)
plt.show()
