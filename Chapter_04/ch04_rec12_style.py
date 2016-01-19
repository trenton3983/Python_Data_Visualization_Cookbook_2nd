import matplotlib.pyplot as plt
import matplotlib
import numpy as np

plt.style.use('mystyle')

x = np.linspace(-2*np.pi, 2*np.pi, 100)
plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()
