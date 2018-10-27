#-*-utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(-2 * math.pi, 2 * math.pi,  math.pi / 32) 

# y = [math.sin(l) + l / math.e for l in x]
y = [math.sin(5 * l) + 2.5 * math.sin(l) for l in x]
plt.title("Complex Funciton")
plt.plot(x, y)

plt.show()
