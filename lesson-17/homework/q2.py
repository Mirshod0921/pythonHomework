import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 3))

x = np.linspace(0, 2 * np.pi, 10000)
z = np.cos(x)
y = np.sin(x)
plt.plot(x, z, linestyle = "-.", marker = "<", color = "k", label = r"$f(x) = \cos(x)$")
plt.legend(loc='upper right')
plt.plot(x, y, linestyle = ":", marker = "o", color = "g", label=r"$f(x) = \sin(x)$")
plt.legend(loc='upper left')
plt.show()