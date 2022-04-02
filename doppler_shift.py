import numpy as np
import matplotlib.pyplot as plt
import math

wavelength = 905 * pow(10, -9)
c = 299702547

speed = np.arange(-50, 50, 0.1)

shift = wavelength * ((c/(c+speed)) - 1)

plt.plot(speed, shift, label = "Shift (nm)")
plt.legend()
plt.show()