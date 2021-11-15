import matplotlib.pyplot as plt
import scipy.special as sps
import numpy as np

k, alpha = 2., 2.  # mean=4, std=2*sqrt(2)
s = np.random.gamma(k, alpha, 10000)

count, bins, ignored = plt.hist(s, 50, density=True)
y = bins**(k-1)*(np.exp(-bins/alpha) /
                     (sps.gamma(k)*alpha**k))
plt.plot(bins, y, linewidth=2, color='r')
plt.show()