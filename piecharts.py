import numpy as np
import matplotlib.pyplot as plt

lang =["Python","Java","C##","C","Javascript"]
points=[40,30,15,9,6]
#pulling items from the chart to highlight them a little bit.Cracking out a little bit
explodes=[0,0,0,0,0.2]

plt.pie(points,labels=lang ,explode=explodes)
plt.show()