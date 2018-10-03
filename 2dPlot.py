import matplotlib.pyplot as plt
# numpy is used fo scientific functionality
import numpy as np

# matplotlib plots points in a line by default
# the first list is the y axis add another list for the x axis
# To remove a connecting line from the plot the third arg is
# shorthand for create blue dots

# numpy range
x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0

# generate noise for the plot
noise = np.random.normal(0.0, 1.0, len(x))

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b.')
plt.plot(x, y + noise, 'r.')
plt.plot(x, y, 'b.')
plt.ylabel("Some Value Label")
plt.show()
