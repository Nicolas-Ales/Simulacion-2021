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

#variables basadas en las constantes de la ruleta
fabs_esperada = n_muestras / len(base)
fr_esperada = 1 / len(base)
media_esperada = np.mean(base)
varianza_esperada = np.var(base)
desviacion_esperada = np.std(base)

def iteracion():

    # listas para los datos almacenados
    data = []
    media = []
    media_media = []
    varianza = []
    varianza_media = []
    desviacion = []

    for i in range(n_muestras):
        data.append(randint(min_n, max_n))
        media.append(np.mean(data))
        media_media.append(np.mean(media))
        desviacion.append(np.std(data))
        if i >= 2:
            varianza.append(st.variance(data))
            varianza_media.append(st.variance(media))

    plot_1(media, media_media, varianza, varianza_media, desviacion)

def preplot():
    # Grafica de media
    plt.subplot(2, 2, 1)
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media')
    plt.title("Media")
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")

    # Grafica de media de media
    plt.subplot(2, 2, 2)
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media de la media')
    plt.title("Media de la media")
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")

    # Grafica de la varianza
    plt.subplot(2, 2, 3)
    plt.title('Varianza')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('varianza')
    plt.plot([0, n_muestras], [varianza_esperada, varianza_esperada], label="varianza esperada")

    plt.subplot(2, 2, 4)
    plt.title('Desviacion estandar')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Desviacion')
    plt.plot([0, n_muestras], [desviacion_esperada, desviacion_esperada], label="desviacion esperada")

def plot_1(m, mm, v, vm, des):
    #Grafica de media
    plt.subplot(2, 2, 1)
    plt.plot(m)
    plt.legend()

    #Grafica de media de media
    plt.subplot(2, 2, 2)
    plt.plot(mm)
    plt.legend()

    #Grafica de la varianza
    plt.subplot(2, 2, 3)
    plt.plot(v)
    plt.legend()

    #Grafica de la desviacion estandar
    plt.subplot(2, 2, 4)
    plt.plot(des)
    plt.legend()

def main():
    seed(801)
    preplot()
    for h in range(0,5):
        iteracion()
        #plot_frAbs(data)
        #plot_frRel(data)
    plt.show()


main()
