import numpy as np
import matplotlib.pyplot as plt
from generadores import *

p = 0.50
n = 30
iteraciones = 10000

x = []
for _ in range(10000):
    x.append(randomBinomial(n, p))
plt.hist(x, density=True, rwidth=0.9, align='mid', bins=20, label='distribucion generada')
# plt.xlim(xmin=0)
plt.title('Distribucion Generada con nuestro codigo')
plt.savefig('binomialGen')
plt.show()

xNP = np.random.binomial(n, p, 10000)
plt.hist(xNP, facecolor='orange', density=True, align='mid', rwidth=0.9, bins=20,
         label='distribucion generada por NunPy')
# plt.xlim(xmin=0)
titulo = 'Distribucion Generada con numpy.binomial('+ str(n) + ','+ str(p) + ')'
plt.title(titulo)
plt.savefig('binomialNP')
plt.show()

print('')
m = np.mean(x)
m1 = n*p
print('Media: ', m, '\nMedia Esperada:', m1)
print('')
v = np.var(x)
v1 = n*p*(1-p)
print('Varianza: ', v, '\nVarianza Esperada:', v1)

mnp = np.mean(xNP)
vnp = np.var(xNP)
print('Media: ', mnp, '\nVarianza: ', vnp)
