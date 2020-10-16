# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-1.5,1.5, 0.01)
y1 = np.exp(x)
y2 = np.exp(-x)
y3 = np.exp(0*x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xticks([0])
# 指定data类型，就是移动到指定数值
# ax.spines['bottom'].set_position('zero')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()