import matplotlib.pyplot as plt
import numpy as np

#### generate png file
x = np.linspace(-10, 10, 1024)
y = np.sinc(x)

plt.plot(x,y,c='k')
plt.show() 
plt.savefig('sinc.png', dpi = 300)
