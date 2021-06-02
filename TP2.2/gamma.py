import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.special as sps
from generadores import *

# Graficando Uniforme
from scipy.interpolate import UnivariateSpline

alpha = 1.5
k = 2
iteraciones = 10000

# s = []
# for _ in range(iteraciones):
#     s.append(randomGamma(alpha, k))
# p, x, ignore = plt.hist(s, bins=20, density=True, rwidth=0.9, align='mid', label='distribucion generada')
# x = x[:-1] + (x[1] - x[0])/2   # convert bin edges to centers
# f = UnivariateSpline(x, p, s=2)
# plt.plot(x, f(x))
# plt.show()

x = []
for _ in range(10000):
    x.append(randomGamma(alpha, k))
plt.hist(x, density=True, rwidth=0.9, align='mid', bins=20, label='distribucion generada')
plt.xlim(xmin=0)
plt.title('Distribucion Generada con nuestro codigo')
plt.savefig('gammaGen')
plt.show()

xNP = np.random.gamma(k, alpha, 10000)
# count, bins,ignored = plt.hist(xNP,50,density=True)
# y = bins**(k-1)*(np.exp(-bins/alpha) /(sps.gamma(k)*alpha**k))
# plt.plot(bins, y, linewidth=2,color='r')
# plt.show()
plt.hist(xNP, facecolor='orange', density=True, align='mid', rwidth=0.9, bins=20,
         label='distribucion generada por NunPy')
plt.xlim(xmin=0)
plt.title('Distribucion Generada con numpy.gamma(2, 1.5)')
plt.savefig('gammaNP')
plt.show()

print('')
m = np.mean(x)
m1 = k / alpha
print('Media: ', m, '\nMedia Esperada:', m1)
print('')
v = np.var(x)
v1 = k / alpha ** 2
print('Varianza: ', v, '\nVarianza Esperada:', v1)

mnp = np.mean(xNP)
vnp = np.var(xNP)
print('Media: ',mnp,'\nVarianza: ',vnp)
