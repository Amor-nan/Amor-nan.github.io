# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,20)
x1=np.linspace(0,10,10)
X=[2,1.5,1,0.5]
y1=[]
for i in range(32):
      y1.append(X[i%4])
fig=plt.figure('16010140048')

plt.subplot(321)
plt.stem(list(y1))
plt.grid(True)
plt.title('zhouqi')

plt.subplot(322)
y2=2*np.sin(0.5*np.pi*x+2)
plt.title('zhengxian')
plt.grid(True)
plt.stem(x,y2)

plt.subplot(323)
y3=[1,0,0,0,0,0,0,0,0]
plt.stem(y3)
plt.grid(True)
plt.title('chongji')

plt.subplot(324)
y4=[0,0,0,1,1,1,1]
plt.stem(y4)
plt.grid(True)
plt.title('jieyue')

plt.subplot(325)
A=2
a=0.6
y5=A*a**x1
plt.grid(True)
plt.title('shizhishu')
plt.stem(x1,y5)

plt.subplot(326)
y5=[8,3.4,1.8,5.6,2.9,0.7]
plt.grid(True)
plt.title('renyi')
plt.stem(y5)



plt.show()