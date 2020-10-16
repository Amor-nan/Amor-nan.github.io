# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-100.0, 100.0, 0.01)
y1 = np.exp(0.01*x)*np.cos(x)
y2 = np.exp(-0.01*x)*np.cos(x)
plt.figure(1)

ax1 = plt.subplot(2,1,1)
ax2 = plt.subplot(2,1,2)

plt.sca(ax1)
plt.plot(x, y1)

plt.sca(ax2)
plt.plot(x, y2)
plt.show()