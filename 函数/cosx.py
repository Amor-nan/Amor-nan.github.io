import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-np.pi,np.pi, 100)
x1 = [t*np.pi for t in x]
y = np.cos(x1)

# 设置线的颜色，粗细，和线型
plt.plot(x, y)

# 如果觉得线条离边界太近了，可以加大距离
plt.xlim(x.min()*1.2, x.max()*1.2)
plt.ylim(y.min()*1.2, y.max()*1.2)

# plt.gca()，全称是get current axis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 指定data类型，就是移动到指定数值
# ax.spines['bottom'].set_position('zero')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()