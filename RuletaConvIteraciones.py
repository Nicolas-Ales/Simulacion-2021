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

# constantes que representan la ruleta
# n_muestras = 1000
min_n = 0
max_n = 36
base = np.arange(37)
nro_elegido = 0

# variables basadas en las constantes de la ruleta
# fabs_esperada = n_muestras / len(base)
fr_esperada = 1 / len(base)
media_esperada = np.mean(base)
varianza_esperada = np.var(base)
desviacion_esperada = np.std(base)


def cambiar_y(x, pos):
    global i
    return x / i


def converge(x, y):
    return y - y * 0.02 <= x <= y + y * 0.02


def plot_1(m, v, des, fr):
    # Grafica de media
    plt.subplot(2, 2, 2)
    plt.plot(m)

    # Grafica de la varianza
    plt.subplot(2, 2, 3)
    plt.plot(v)

    # Grafica de la desviacion estandar
    plt.subplot(2, 2, 4)
    plt.plot(des)

    # Grafica de Frecuencia Relativa del Nro_elegido
    plt.subplot(2, 2, 1)
    plt.plot(fr)

def post_plot():
    # Grafica de media
    plt.subplot(2, 2, 2)
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media')
    plt.title("Media")
    plt.plot([0, i], [media_esperada, media_esperada], label="media esperada")
    plt.legend()

    # Grafica de la varianza
    plt.subplot(2, 2, 3)
    plt.title('Varianza')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('varianza')
    plt.plot([0, i], [varianza_esperada, varianza_esperada], label="varianza esperada")
    plt.legend()

    # Grafica de la desviacion estandar
    plt.subplot(2, 2, 4)
    plt.title('Desviacion estandar')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Desviacion')
    plt.plot([0, i], [desviacion_esperada, desviacion_esperada], label="desviacion esperada")
    plt.legend()

    # Grafica de Frecuencia Relativa del Nro_elegido
    plt.subplot(2, 2, 1)
    plt.title('Frecuencia Relativa')
    plt.axhline(y=1 / len(base),label="FR Esperada")
    #plt.plot([0, i], [1 / len(base), 1 / len(base)], label="FR Esperada")
    plt.legend(loc="upper right")
    plt.ylabel('FR para el numero ' + str(nro_elegido))
    plt.xlabel('n(numero de tiradas)')
    plt.show()

def ietracion():
    data = []
    media = []
    varianza = []
    desviacion = []
    fr = []
    global i
    j = 0
    i = 0
    count = 0
    while True:
        rand = randint(min_n, max_n)
        data.append(rand)
        media.append(np.mean(data))
        desviacion.append(np.std(data))
        if i >= 2:
            varianza.append(st.variance(data))
        if rand == nro_elegido:
            count += 1
        fr.append(count / (i + 1))

        i = i + 1
        convergencia = converge(np.mean(data), media_esperada) and converge(np.std(data), desviacion_esperada) and \
                       converge(st.variance(data), varianza_esperada)
        if convergencia:
            j = j + 1
            #print(j)
        else:
            j = 0

        if j >= 100:
            break
    print("Numero de Lanzamientos: ", i)
    plot_1(media, varianza, desviacion, fr)

def main():
    seed(801)
    for k in range(0,5):
        ietracion()
    post_plot()



main()