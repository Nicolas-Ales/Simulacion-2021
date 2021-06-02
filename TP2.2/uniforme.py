import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from generadores import *

# Graficando Uniforme

x = []
for _ in range(10000):
    x.append(randomUniforme(0, 10))
plt.hist(x, density=True, rwidth=0.9, align='mid', bins=20, label='distribucion generada')
plt.xlim(0, 10)
plt.title('Distribucion Generada con nuestro codigo')

rv = stats.uniform()
plt.axhline(0.10, label='algo', color='red')
print(stats.uniform.fit(x))
# plt.savefig('uniformeGen')
plt.show()
#
# xNP = np.random.uniform(low=0, high=10, size=10000)
# plt.hist(xNP, facecolor='orange', density=True, align='mid', rwidth=0.9, bins=20,
#          label='distribucion generada por NunPy')
# plt.legend()
# plt.xlim(0, 10)
# plt.title('Distribucion Generada con NunPy.uniform()')
# plt.savefig('uniformeNP')
# plt.show()
#
# print('')
# m = np.mean(x)
# m1 = (10 - 0) / 2
# print('Media: ', m, '\nMedia Esperada:', m1)
# print('')
# v = np.var(x)
# v1 = ((10 - 0) ** 2) / 12
# print('Varianza: ', v, '\nVarianza Esperada:', v1)
