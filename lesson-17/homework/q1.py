import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 6, 10000)
def f_x(x):
    return x**2 - 4*x + 4

y = f_x(x)
plt.plot(x, y, label='$f(x) = x^2 - 4x + 4$')
plt.title('Parabola')
plt.xlabel('X')
plt.ylabel('Y', rotation=0)
plt.legend()
plt.show()