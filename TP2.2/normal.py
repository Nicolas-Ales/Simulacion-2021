import numpy as np
import matplotlib.pyplot as plt
from generadores import *

mu = 1.5
sigma = 0.2
k = 5
iteraciones = 10000

x = []
for _ in range(10000):
    x.append(randomNormal(mu,sigma,k))
plt.hist(x, density=True, rwidth=0.9, align='mid', bins=20, label='distribucion generada')
#plt.xlim(xmin=0)
plt.title('Distribucion Generada con nuestro codigo')
plt.savefig('normalGen')
plt.show()

xNP = np.random.normal(mu,sigma, 10000)
plt.hist(xNP, facecolor='orange', density=True, align='mid', rwidth=0.9, bins=20,
         label='distribucion generada por NunPy')
#plt.xlim(xmin=0)
plt.title('Distribucion Generada con numpy.normal(1.5,0.2)')
plt.savefig('normalNP')
plt.show()

print('')
m = np.mean(x)
m1 = mu
print('Media: ', m, '\nMedia Esperada:', m1)
print('')
v = np.var(x)
v1 = sigma**2
print('Varianza: ', v, '\nVarianza Esperada:', v1)

mnp = np.mean(xNP)
vnp = np.var(xNP)
print('Media: ',mnp,'\nVarianza: ',vnp)