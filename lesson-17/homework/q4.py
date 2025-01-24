import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0,11,100)
y = np.random.randint(0,11,100)

plt.scatter(x, y, c = y, marker = "H",cmap = "cool")

plt.title("Scatter plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.show()