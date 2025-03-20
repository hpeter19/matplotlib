import numpy as np
import matplotlib.pyplot as plt

years= [2016,2017,2018,2019,2020,2021,2022,2023]
income =[56,61,65,70,72,76,82,90]
income_ticks =list(range(50,81,2))
plt.plot(years,income)
plt.title("Income of John(In Ksh)")
plt.xlabel("Year")
plt.ylabel("Income in Ksh")
plt.yticks(income_ticks,[f"{x}k Ksh" for x in income_ticks])
plt.show()