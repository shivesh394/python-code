import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints,marker='p')
plt.plot(ypoints, 'o:r',ms=20)
plt.show()