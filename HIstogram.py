import matplotlib.pyplot as plt

import numpy as np

x = np.random.normal(0.0, 1.0, 1000)
# bins param to have more fine grain chart
plt.hist(x, bins=40)

plt.show()