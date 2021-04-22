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
n_muestras = 2500
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


def plot_1(m, mm, v, des, fr):
    # Grafica FRelativa
    plt.figure(figsize=(6, 3.4))
    plt.title('Frecuencia Relativa')
    for frec in fr:
        plt.plot(frec)
    plt.axhline(fr_esperada, color='red', label='frecuencia esperada')
    plt.legend(loc="upper right")
    plt.ylabel('FR para el numero ' + str(nro_elegido))
    plt.xlabel('n(numero de tiradas)')
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.ylim(0)
    plt.savefig('frecuencia relativa iteraciones', bbox_inches = "tight")
    plt.show()

    # Grafica de media
    plt.figure(figsize=(6, 3.4))
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media')
    plt.title("Media")
    for mean in m:
        plt.plot(mean)
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    plt.legend()
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.savefig('media iteraciones', bbox_inches = "tight")
    plt.show()

    # Grafica de media de media
    plt.figure(figsize=(6, 3.4))
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media de la media')
    plt.title("Media de la media")
    for meanm in mm:
        plt.plot(meanm)
    plt.plot([0, n_muestras], [media_esperada, media_esperada], label="media esperada")
    plt.legend()
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.savefig('media de media iteraciones', bbox_inches = "tight")
    plt.show()

    # Grafica de la varianza
    plt.figure(figsize=(6, 3.4))
    plt.title('Varianza')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Varianza')
    for var in v:
        plt.plot(var)
    plt.axhline(varianza_esperada, label="varianza esperada", color='red')
    plt.legend()
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.savefig('varianza iteraciones', bbox_inches = "tight")
    plt.show()

    # Grafica de la desviacion estandar
    plt.figure(figsize=(6, 3.4))
    plt.title('Desviacion estandar')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Desviacion')
    for d in des:
        plt.plot(d)
    plt.plot([0, n_muestras], [desviacion_esperada, desviacion_esperada], label="desviacion esperada")
    plt.legend()
    plt.xlim(xmin=0, xmax=n_muestras)
    plt.ylim(ymin=0)
    plt.savefig('desviacion estandar iteraciones', bbox_inches = "tight")
    plt.show()


def main():
    seed(801)
    count = 0
    datas = []
    medias = []
    medias_medias = []
    desviaciones = []
    varianzas = []
    frecuencias = []
    for j in range(50):
        data = []
        media = []
        media_media = []
        desviacion = []
        varianza = []
        f_relativas = []
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
        print(j, '\n', f_relativas)
        datas.append(data)
        medias.append(media)
        medias_medias.append(media_media)
        desviaciones.append(desviacion)
        varianzas.append(varianza)
        frecuencias.append(f_relativas)
    print(frecuencias)
    plot_1(medias, medias_medias, varianzas, desviaciones, frecuencias)


main()
