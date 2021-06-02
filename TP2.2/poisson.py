import numpy as np
import matplotlib.pyplot as plt
from generadores import *

lamd = 15 #Lamnda
iteraciones = 10000

x = []
for _ in range(10000):
    x.append(randomPoisson(lamd))
plt.hist(x, density=True, rwidth=0.9, align='mid', bins=30, label='distribucion generada')
# plt.xlim(xmin=0)
plt.title('Distribucion Generada con nuestro codigo')
plt.savefig('poissonGen')
plt.show()


xNP = np.random.poisson(lamd, 10000)
plt.hist(xNP, facecolor='orange', density=True, align='mid', rwidth=0.9, bins=30,
         label='distribucion generada por NunPy')
# plt.xlim(xmin=0)
titulo = 'Distribucion Generada con numpy.hypergeometric(' + str(lamd) + ')'
plt.title(titulo)
plt.savefig('poissonNP')
plt.show()

print('')
m = np.mean(x)
m1 = lamd
print('Media: ', m, '\nMedia Esperada:', m1)
print('')
v = np.var(x)
v1 = lamd
print('Varianza: ', v, '\nVarianza Esperada:', v1)

mnp = np.mean(xNP)
vnp = np.var(xNP)
print('Media: ', mnp, '\nVarianza: ', vnp)
