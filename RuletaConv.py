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

# listas para los datos almacenados
data = []
media = []
media_media = []
varianza = []
varianza_media = []
desviacion = []
fr = []

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


# def plot_frAbs(d):  # graficar histograma de frecuencias absolutas
#     fig, ax = plt.subplots()
#     ax.hist(d, bins=max_n + 1, edgecolor="black")
#     ax.axhline(y=fabs_esperada, color="yellow", label="frecuencia esperada")
#     fig.tight_layout()
#     ax.set_xlabel('Numeros de la ruleta')
#     ax.set_ylabel('Cantidad')
#     plt.title("Histograma de frecuencia absoluta")
#     plt.legend()
#     plt.show()


def plot_frRel(d,i):  # graficar histograma de frecuencias relativas
    fig, ax = plt.subplots()
    ax.hist(d, bins=max_n + 1, edgecolor="grey")
    ax.yaxis.set_major_formatter(tick.FuncFormatter(cambiar_y))  # para cambiar los valores mostrados en y
    ax.axhline(y=fr_esperada * i, color="yellow",
               label="frecuencia esperada")  # se multiplica x 1000 la frecuencia por la modificacion anterior
    fig.tight_layout()
    ax.set_xlabel('Numeros de la ruleta')
    ax.set_ylabel('Cantidad / 100')
    plt.title("Histograma de frecuencia relativa")
    plt.legend(handlelength=4)
    plt.show()
    print(d)
    print(i)


def plot_1(m, mm, v, vm, des, i, fr):
    # Grafica de media
    plt.subplot(2, 2, 2)
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media')
    plt.title("Media")
    plt.plot(m, label="media")
    # plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    plt.plot([0, i], [media_esperada, media_esperada], label="media esperada")
    plt.legend()

    # # Grafica de media de media
    # plt.xlabel('Cantidad de tiradas')
    # plt.ylabel('Media de la media')
    # plt.title("Media de la media")
    # plt.plot(mm, label="media de la media")
    # # plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    # plt.plot([0, i], [media_esperada, media_esperada], label="media esperada")
    # plt.legend()
    # plt.show()

    # # Grafica que relaciona media y media de media
    # plt.plot(list(range(len(m))), m, label="media")
    # plt.plot(list(range(len(mm))), mm, color='r', linestyle="-.", label="media de media")
    # # plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    # plt.plot([0, i], [media_esperada, media_esperada], label="media esperada")
    # plt.xlabel('Cantidad de tiradas')
    # plt.ylabel('Medias')
    # plt.title("Relacion entre media y media de media")
    # plt.legend()
    # plt.show()

    # Grafica de la varianza
    plt.subplot(2, 2, 3)
    plt.title('Varianza')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('varianza')
    plt.plot(v, label="varianza")
    # plt.plot([0, n_muestras], [varianza_esperada, varianza_esperada], label="varianza esperada")
    plt.plot([0, i], [varianza_esperada, varianza_esperada], label="varianza esperada")
    plt.legend()

    # Grafica de la desviacion estandar
    plt.subplot(2, 2, 4)
    plt.title('Desviacion estandar')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Desviacion')
    plt.plot(des, label="desviacion estandar")
    # plt.plot([0, n_muestras], [desviacion_esperada, desviacion_esperada], label="desviacion esperada")
    plt.plot([0, i], [desviacion_esperada, desviacion_esperada], label="desviacion esperada")
    plt.legend()

    # Grafica de Frecuencia Relativa del Nro_elegido
    plt.subplot(2, 2, 1)
    plt.title('Frecuencia Relativa')
    plt.plot(fr)
    plt.plot([0, i], [1 / len(base), 1 / len(base)], label="FR Esperada")
    plt.legend(loc="upper right")
    plt.ylabel('FR para el numero ' + str(nro_elegido))
    plt.xlabel('n(numero de tiradas)')
    plt.show()


def main():
    seed(801)
    global i
    j = 0
    i = 0
    count = 0
    while True:
        rand = randint(min_n, max_n)
        data.append(rand)
        media.append(np.mean(data))
        media_media.append(np.mean(media))
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
            print(j)
        else:
            j = 0

        if j >= 100:
            break


    # plot_frAbs(data)
    #plot_frRel(data, i)
    print("Numero de Lanzamientos: ",i)
    plot_1(media, media_media, varianza, varianza_media, desviacion, i, fr)


main()
