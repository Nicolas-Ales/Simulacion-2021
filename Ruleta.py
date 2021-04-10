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
n_muestras = 1000
min_n = 0
max_n = 36
base = np.arange(37)

# listas para los datos almacenados
data = []
media = []
media_media = []
varianza = []
varianza_media = []
desviacion = []

# variables basadas en las constantes de la ruleta
fabs_esperada = n_muestras / len(base)
fr_esperada = 1 / len(base)
media_esperada = np.mean(base)
varianza_esperada = np.var(base)
desviacion_esperada = np.std(base)


def cambiar_y(x, pos):
    return x / len(data) * 1.0


def plot_frAbs(f,n):  # graficar histograma de frecuencias absolutas
    plt.bar(n,f,edgecolor='black')
    plt.axhline(y=fabs_esperada, color="yellow", label="frecuencia esperada")
    plt.xlabel('Numeros de la ruleta')
    plt.ylabel('Frecuencia relativa')
    plt.title("Histograma de frecuencia absoluta")
    plt.legend()
    plt.savefig('FAbs')
    plt.show()


def plot_frRel(f,n):  # graficar histograma de frecuencias relativas
    fr =[]
    for frec in f:
        fr.append(frec/n_muestras)
    plt.bar(n,fr,edgecolor='black')
    plt.axhline(y=fr_esperada, color="yellow", label="frecuencia esperada")
    plt.xlabel('Numeros de la ruleta')
    plt.ylabel('Frecuencia relativa')
    plt.legend()
    plt.savefig('FRel')
    plt.show()


def plot_1(m, mm, v, vm, des):
    # Grafica de media
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media')
    plt.title("Media")
    plt.plot(m, label="media")
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    plt.legend()
    plt.xlim(xmin=0)
    plt.savefig('Media')
    plt.show()

    # Grafica de media de media
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media de la media')
    plt.title("Media de la media")
    plt.plot(mm, label="media de la media")
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    plt.legend()
    plt.xlim(xmin=0)
    plt.savefig('Media de Medias')
    plt.show()

    # Grafica que relaciona media y media de media
    plt.plot(list(range(len(m))), m, label="media")
    plt.plot(list(range(len(mm))), mm, color='r', linestyle="-.", label="media de media")
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Medias')
    plt.title("Relacion entre media y media de media")
    plt.legend()
    plt.xlim(xmin=0)
    plt.savefig('RelacionMedias')
    plt.show()

    # Grafica de la varianza
    plt.title('Varianza')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('varianza')
    plt.plot(v, label="varianza")
    plt.plot([0, n_muestras], [varianza_esperada, varianza_esperada], label="varianza esperada")
    plt.legend()
    plt.xlim(xmin=0)
    plt.savefig('Varianza')
    plt.show()

    # Grafica de la desviacion estandar
    plt.title('Desviacion estandar')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Desviacion')
    plt.plot(des, label="desviacion estandar")
    plt.plot([0, n_muestras], [desviacion_esperada, desviacion_esperada], label="desviacion esperada")
    plt.legend()
    plt.xlim(xmin=0)
    plt.savefig('DesvEstandar')
    plt.show()


def main():
    seed(801)
    for i in range(n_muestras):
        data.append(randint(min_n, max_n))
        media.append(np.mean(data))
        media_media.append(np.mean(media))
        desviacion.append(np.std(data))
        if i >= 2:
            varianza.append(st.variance(data))
            varianza_media.append(st.variance(media))
    frec = []
    nros = []
    for n in range(37):
        count = sum(map(lambda x: x == n, data))
        frec.append(count)
        nros.append(n)
    print(frec)
    print(nros)

    plot_frAbs(frec,nros)
    plot_frRel(frec,nros)
    plot_1(media, media_media, varianza, varianza_media, desviacion)


main()
