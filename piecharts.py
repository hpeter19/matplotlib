import numpy as np
import matplotlib.pyplot as plt

lang =["Python","Java","C##","C","Javascript"]
points=[40,30,15,9,6]

plt.pie(points,labels=lang)
plt.show()