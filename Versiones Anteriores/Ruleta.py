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
nro_elegido = 0

# listas para los datos almacenados
data = []
media = []
media_media = []
varianza = []
varianza_media = []
desviacion = []
f_relativas = []

# variables basadas en las constantes de la ruleta
fabs_esperada = n_muestras / len(base)
fr_esperada = 1 / len(base)
media_esperada = np.mean(base)
varianza_esperada = np.var(base)
desviacion_esperada = np.std(base)


def cambiar_y(x, pos):
    return x / len(data) * 1.0


def plot_frAbs(f, n):  # graficar histograma de frecuencias absolutas
    plt.figure(figsize=(6, 3.4))
    plt.bar(n, f, edgecolor='black')
    plt.axhline(y=fabs_esperada, color="yellow", label="frecuencia esperada")
    plt.xlabel('Numeros de la ruleta')
    plt.ylabel('Frecuencia relativa')
    plt.title("Histograma de frecuencia absoluta")
    plt.legend()
    plt.savefig('histograma de frecuencia absoluta', bbox_inches="tight")
    plt.show()


def plot_frRel(f, n):  # graficar histograma de frecuencias relativas
    fr = []
    for frec in f:
        fr.append(frec / n_muestras)
    plt.figure(figsize=(6, 3.4))
    plt.bar(n, fr, edgecolor='black')
    plt.axhline(y=fr_esperada, color="yellow", label="frecuencia esperada")
    plt.xlabel('Numeros de la ruleta')
    plt.ylabel('Frecuencia relativa')
    plt.legend()
    plt.savefig('histograma de frecuencia absoluta', bbox_inches="tight")
    plt.show()


def plot_1(m, mm, v, vm, des, fr):
    # Grafica FRelativa
    plt.figure(figsize=(6, 3.4))
    plt.title('Frecuencia Relativa')
    plt.plot(fr)
    plt.axhline(fr_esperada, color='red', label='frecuencia esperada')
    plt.legend(loc="upper right")
    plt.ylabel('FR para el numero ' + str(nro_elegido))
    plt.xlabel('n(numero de tiradas)')
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.ylim(0)
    plt.savefig('frecuencia relativa', bbox_inches="tight")
    plt.show()

    # Grafica de media
    plt.figure(figsize=(6, 3.4))
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media')
    plt.title("Media")
    plt.plot(m, label="media")
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    plt.legend()
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.savefig('media', bbox_inches="tight")
    plt.show()

    # Grafica de media de media
    plt.figure(figsize=(6, 3.4))
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media de la media')
    plt.title("Media de la media")
    plt.plot(mm, label="media de la media")
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    plt.legend()
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.savefig('media de media', bbox_inches="tight")
    plt.show()

    # Grafica que relaciona media y media de media
    plt.figure(figsize=(6, 3.4))
    plt.plot(list(range(len(m))), m, label="media")
    plt.plot(list(range(len(mm))), mm, color='r', linestyle="-.", label="media de media")
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Medias')
    plt.title("Relacion entre media y media de media")
    plt.legend()
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.savefig('relacion entre media y media de medias', bbox_inches="tight")
    plt.show()

    # Grafica de la varianza
    plt.figure(figsize=(6, 3.4))
    plt.title('Varianza')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Varianza')
    plt.plot(v, label="varianza")
    plt.plot([0, n_muestras], [varianza_esperada, varianza_esperada], label="varianza esperada")
    plt.legend()
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.savefig('varianza', bbox_inches="tight")
    plt.show()

    # Grafica de la desviacion estandar
    plt.figure(figsize=(6, 3.4))
    plt.title('Desviacion estandar')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Desviacion')
    plt.plot(des, label="desviacion estandar")
    plt.plot([0, n_muestras], [desviacion_esperada, desviacion_esperada], label="desviacion esperada")
    plt.legend()
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.ylim(ymin=0)
    plt.savefig('desviacion estandar', bbox_inches="tight")
    plt.show()


def main():
    seed(801)
    count = 0
    for i in range(1, n_muestras):
        n = randint(min_n, max_n)
        if n == nro_elegido:
            count += 1
        f_relativas.append(count / i)
        data.append(n)
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

    plot_frAbs(frec, nros)
    plot_frRel(frec, nros)
    plot_1(media, media_media, varianza, varianza_media, desviacion, f_relativas)


main()
