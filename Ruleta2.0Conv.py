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
    plt.xlim(xmin=0)
    plt.ylim(0)
    plt.savefig('frecuencia relativa convergencia iteraciones', bbox_inches="tight")
    plt.show()

    # Grafica de media
    plt.figure(figsize=(6, 3.4))
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media')
    plt.title("Media")
    plt.axhline(y=media_esperada + media_esperada * 0.02, color="yellow", linestyle='dashed')
    plt.axhline(y=media_esperada - media_esperada * 0.02, color="yellow", linestyle='dashed')
    for mean in m:
        plt.plot(mean)
    plt.axhline(media_esperada, color='red', label='media esperada')
    plt.legend()
    plt.xlim(xmin=0)
    plt.savefig('media convergencia iteraciones', bbox_inches="tight")
    plt.show()

    # Grafica de media de media
    plt.figure(figsize=(6, 3.4))
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Media de la media')
    plt.title("Media de la media")
    for meanm in mm:
        plt.plot(meanm)
    plt.axhline(media_esperada, color='red', label='media esperada')
    plt.legend()
    plt.xlim(xmin=0)
    plt.savefig('media de media convergencia iteraciones', bbox_inches="tight")
    plt.show()

    # Grafica de la varianza
    plt.figure(figsize=(6, 3.4))
    plt.title('Varianza')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Varianza')
    plt.axhline(y=varianza_esperada + varianza_esperada * 0.02, color="yellow", linestyle='dashed')
    plt.axhline(y=varianza_esperada - varianza_esperada * 0.02, color="yellow", linestyle='dashed')
    for var in v:
        plt.plot(var)
    plt.axhline(varianza_esperada, label="varianza esperada", color='red')
    plt.legend()
    plt.xlim(xmin=0)
    plt.savefig('varianza convergencia iteraciones', bbox_inches="tight")
    plt.show()

    # Grafica de la desviacion estandar
    plt.figure(figsize=(6, 3.4))
    plt.title('Desviacion estandar')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('Desviacion')
    plt.axhline(y=desviacion_esperada + desviacion_esperada * 0.02, color="yellow", linestyle='dashed')
    plt.axhline(y=desviacion_esperada - desviacion_esperada * 0.02, color="yellow", linestyle='dashed')
    for d in des:
        plt.plot(d)
    plt.axhline(desviacion_esperada, color='red', label='desviacion esperada')
    plt.legend()
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.savefig('desviacion estandar convergencia iteraciones', bbox_inches="tight")
    plt.show()


def converge(x, y):
    return y - y * 0.02 <= x <= y + y * 0.02


def main():
    seed(801)
    count = 0
    datas = []
    medias = []
    medias_medias = []
    desviaciones = []
    varianzas = []
    frecuencias = []
    for k in range(1):
        data = []
        media = []
        media_media = []
        desviacion = []
        varianza = []
        f_relativas = []
        count = 0
        i = 1
        while True:
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
            i += 1
            convergencia = converge(np.mean(data), media_esperada) and converge(np.std(data), desviacion_esperada) and \
                           converge(st.variance(data), varianza_esperada)
            if convergencia:
                j = j + 1
            else:
                j = 0

            if j >= 100:
                break
        print("Numero de Lanzamientos: ", i)
        datas.append(data)
        medias.append(media)
        medias_medias.append(media_media)
        desviaciones.append(desviacion)
        varianzas.append(varianza)
        frecuencias.append(f_relativas)
    plot_1(medias, medias_medias, varianzas, desviaciones, frecuencias)


main()
