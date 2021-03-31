# Como ejercicio tenemos que hacer una ruleta y hacer las graficas
# 1- fr/n frecuencia relativa #cantidad de veces que SALIO el numero / cantidad total de muestras
# 2- vp/n valor promedio de las tiradas
# 3- vd/n valor del desvio       np.std(datos, 0) # Desviación típica de cada columna
# 4- vv/n valor de la varianza
import numpy as np
import matplotlib.pyplot as plt
import random as rn
import matplotlib.ticker as tick
import statistics as st
from random import randint, seed

#constantes que representan la ruleta
n_muestras = 1000
min_n = 0
max_n = 36
base = np.arange(37)
nro_elegido = 0

#variables basadas en las constantes de la ruleta
fr_esperada = 1 / len(base)


def iteracion():
    fr = []
    count = 0
    for i in range(n_muestras):
        rand = randint(min_n, max_n)
        if rand == nro_elegido:
            count += 1
        fr.append(count / (i + 1))
    plt.plot(fr)

def preplot():

    plt.title('Frecuencia Relativa')
    plt.plot([0, n_muestras], [1 / len(base), 1 / len(base)], label="FR Esperada")
    plt.legend(loc="upper right")
    plt.ylabel('FR para el numero ' + str(nro_elegido))
    plt.xlabel('n(numero de tiradas)')

def main():
    seed(801)
    preplot()
    for h in range(0,5):
        iteracion()
    plt.show()


main()
