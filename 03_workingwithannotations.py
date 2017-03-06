import numpy as np
import matplotlib.pyplot as plt

#### add title,axis lables,text
'''
X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

# plt.title('A polynomial') #addind title
# plt.title('$f(x)=\\frac{1}{4}(x+4)(x+1)(x-2)$') #using latex-style notations
plt.title('Power curve for airfoil KV873')
# plt.text(-0.5, -0.25, 'Brackmard minimum') # adding text

### adding box control
box = {
	'facecolor': '.75',
	'edgecolor' : 'k',
	'boxstyle': 'round'
}

plt.text(-0.5, -0.20, 'Brackmard minimum', bbox = box)

### adding arrow
plt.annotate('Brackmard minimum',
ha = 'center', va = 'bottom',
xytext = (-1.5, 3.),
xy = (0.75, -2.7),
arrowprops = { 'facecolor' : 'black', 'shrink' : 0.05 })

plt.xlabel('Air speed') # adding x axis lable
plt.ylabel('Total drag')
plt.plot(X, Y,  c = 'k')
plt.show()
'''

#### adding a legend(图例)
x = np.linspace(-4,4,1024)

y1 = np.sin(x)
y2 = np.cos(x)

plt.xlabel('x')
plt.ylabel('y')

plt.plot(x, y1, c = 'k', lw = 3., label = 'sin(x)')
plt.plot(x, y2, c = '.5', lw = 3., ls = '--', label = 'cos(x)')

plt.legend()
plt.show()
