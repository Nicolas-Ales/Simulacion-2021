import numpy as np
import matplotlib.pyplot as plt
from generadores import *

N = 500  # Tamaño de poblacion
n = 300  # numero de sorteos
p = 0.25  # Probabilidad de que salga positivo K/N
K = N * p
iteraciones = 10000

x = []
for _ in range(10000):
    x.append(randomHipergeometrica(N, n, p))
plt.hist(x, density=True, rwidth=0.9, align='mid', bins=20, label='distribucion generada')
# plt.xlim(xmin=0)
plt.title('Distribucion Generada con nuestro codigo')
plt.savefig('hipergeometricaGen')
plt.show()


xNP = np.random.hypergeometric(K, N-K, n, 10000)
plt.hist(xNP, facecolor='orange', density=True, align='mid', rwidth=0.9, bins=20,
         label='distribucion generada por NunPy')
# plt.xlim(xmin=0)
titulo = 'Distribucion Generada con numpy.hypergeometric(' + str(K) + ',' + str(N) + '-' + str(K) + ',' + str(n) + ')'
plt.title(titulo)
plt.savefig('hipergeometricaNP')
plt.show()

print('')
m = np.mean(x)
m1 = n*K/N
print('Media: ', m, '\nMedia Esperada:', m1)
print('')
v = np.var(x)
v1 = n*p*(1-p)*(N-n)/(N-1)
print('Varianza: ', v, '\nVarianza Esperada:', v1)

mnp = np.mean(xNP)
vnp = np.var(xNP)
print('Media: ', mnp, '\nVarianza: ', vnp)
