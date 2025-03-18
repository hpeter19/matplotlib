import numpy as np
import matplotlib.pyplot as plt



x_data= np.random.random(50)*100
y_data = np.random.random(50) * 100
#adjusting the color,the marker and transparency
plt.scatter(x_data,y_data,c="red",marker="*",s=150,)
plt.show()
