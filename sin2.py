import matplotlib.pyplot as plt
import numpy as np

# curve multipic
'''x = np.linspace(0, 2 * np.pi, 100)
ya = np.sin(x)
yb = np.cos(x)

plt.plot(x,ya)
plt.plot(x,yb)
plt.show()'''

# plot slope
'''def plot_slope(X, Y): 
	Xs = X[1:] - X[:-1] 
	Ys = Y[1:] - Y[:-1] 
	plt.plot(X[1:], Ys / Xs) 
	
X = np.linspace(-3, 3, 100) 
Y = np.exp(-X ** 2) 

plt.plot(X, Y) 
plot_slope(X, Y) # slope:斜率
plt.show()'''

#plot curve from file
'''x = []
y = []
for line in open('0.txt', 'r'):
	v = [float(s) for s in line.split(',')]
	x.append(v[0])
	y.append(v[1])
	
plt.plot(x,y)
plt.show()'''

'''with open('0.txt','r') as f:
	x,y = zip(*[[float(s) for s in line.split(',')] for line in f])
	
plt.plot(x,y)
plt.show()'''

'''data = np.loadtxt('0.txt') #txt不能含有字符串
#print(data)

plt.plot(data[:,0],data[:,1])
plt.show()'''

'''data = np.loadtxt('1.txt')

for column in data.T:
	plt.plot(data[:,0], column)

plt.show()'''

'''data = np.random.rand(1024, 2) #1024行2列，数值为0到1之间的随机数

plt.scatter(data[:,0], data[:, 1])
plt.show()'''

'''data = [5., 25.,50., 20.]
plt.bar(range(len(data)), data)
plt.show()

plt.bar(range(len(data)), data, width=1.)
plt.show()

plt.barh(range(len(data)), data) #绘制水平直方图，在ios上出错，同时出现水平和垂直两种
plt.show()'''


