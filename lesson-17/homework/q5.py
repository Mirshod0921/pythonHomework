import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(data, bins=30, color="g", edgecolor = "k", alpha = 0.8)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()