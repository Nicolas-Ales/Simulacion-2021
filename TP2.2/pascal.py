import numpy as np
import matplotlib.pyplot as plt
from generadores import *

q = 0.50
k = 100
iteraciones = 10000

x = []
for _ in range(10000):
    x.append(randomPascal(k, q))
plt.hist(x, density=True, rwidth=0.9, align='mid', bins=20, label='distribucion generada')
# plt.xlim(xmin=0)
plt.title('Distribucion Generada con nuestro codigo')
#plt.savefig('pascalGen')
plt.show()

xNP = np.random.negative_binomial(k, q, 10000)
plt.hist(xNP, facecolor='orange', density=True, align='mid', rwidth=0.9, bins=20,
         label='distribucion generada por NunPy')
# plt.xlim(xmin=0)
titulo = 'Distribucion Generada con numpy.negative_binomial('+ str(k) + ','+ str(q) + ')'
plt.title(titulo)
#plt.savefig('pascalNP')
plt.show()

print('')
m = np.mean(x)
m1 = k*(1-q)/q
print('Media: ', m, '\nMedia Esperada:', m1)
print('')
v = np.var(x)
v1 = k*(1-q)/q**2
print('Varianza: ', v, '\nVarianza Esperada:', v1)

mnp = np.mean(xNP)
vnp = np.var(xNP)
print('Media: ', mnp, '\nVarianza: ', vnp)
