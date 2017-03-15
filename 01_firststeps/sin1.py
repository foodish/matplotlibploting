import math
import matplotlib.pyplot as plt

t = range(100)
x = [2 * math.pi * i / len(t) for i in t]
y = [math.sin(i) for i in x]

plt.plot(x,y)
plt.show()
