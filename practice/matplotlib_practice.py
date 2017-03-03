import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(100000)

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
y = mlab.normpdf(bins, mu, sigma)
# add a 'best fit' line
plt.plot(bins, y, 'r')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of y label
plt.subplots_adjust(left=0.15)
plt.show()
