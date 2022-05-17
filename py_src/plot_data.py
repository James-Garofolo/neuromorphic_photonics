import matplotlib.pyplot as plt
import numpy as np
import os





x = np.array([range(0, 10), range(0, 10), range(0, 10)])
y = np.array([np.ones(10), np.ones(10)*2, np.ones(10)*3])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y)

plt.show()