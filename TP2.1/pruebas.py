from scipy.stats import ksone
import math
import numpy as np


def pruebaKS(muestra):
    # Prueba de Kolmogorov-Smirnov
    n = len(muestra)
    muestra_ordenada = muestra.copy()
    muestra_ordenada.sort()
    d_esperada = (ksone.ppf((1 - 0.05 / 2), n))
    # 1.36/math.sqrt(n)
    d_mas = []
    d_menos = []

    for i in range(1, n + 1):
        x = i / n - muestra_ordenada[i - 1]
        d_mas.append(x)

    for i in range(1, n + 1):
        y = (i - 1) / n
        y = muestra_ordenada[i - 1] - y
        d_menos.append(y)

    D = max(max(d_mas, d_menos))
    print("D calculada: " + str(D) + " , D esperada : " + str(d_esperada))
    if (D < d_esperada):
        print("Test aprobado. Muestra uniforme")
        print("")
        return True
    else:
        print("Test desaprobado. No implica que no sea uniforme")
        print("")
        return False


def pruebaChiCuadrado(muestra):
    valorTabla = 16.9190  # con alpha 0.05 y grado de libertad 9
    f_esperada = len(muestra) / 10
    muestra_ordenada = muestra.copy()
    muestra_ordenada.sort()
    frec = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    intervalo = 0
    for i in range(0, 10):
        for j in range(len(muestra)):
            if intervalo <= muestra_ordenada[j] < (intervalo + 0.1):
                frec[i] += 1
        intervalo += 0.1

    chiCuadrado = 0
    for k in range(0, 10):
        chiCuadrado += ((frec[k] - f_esperada) ** 2) / f_esperada
    print(chiCuadrado)
    if chiCuadrado < valorTabla:
        print("Test aprobado. Muestra uniforme")
        print("")
        return True
    else:
        print("Test desaprobado. No implica que no sea uniforme")
        print("")
        return False

    print(valorTabla)


def pruebaParidad(muestra):
    n = len(muestra)
    par = 0
    inpar = 0
    for m in muestra:
        if (math.floor(m * 10000) % 2) == 0:
            par += 1
        else:
            inpar += 1
    frec = par / n
    if 0.45 <= frec <= 0.55:
        print(
            "Test aprobado. Muestra aleatoria, las frecuencias de las paridades se encuentran en el rango de aceptación")
        print("")
        return True
    else:
        print("Test desaprobado. Muestra con números mayormente de una paridad notablemente")
        print("")
        return False


def pruebaRachas(muestra):
    listaOperadores = []
    N = len(muestra)
    n1 = 0
    n2 = 0
    b = 0
    mediaMuestra = np.average(muestra)
    mediaB = 0
    varianzaB = 0
    Z = 0
    for l in muestra:
        if l >= mediaMuestra:
            listaOperadores.append('+')
            n1 += 1
        else:
            listaOperadores.append('-')
            n2 += 1
    for j in range(0, len(listaOperadores) - 1):
        if listaOperadores[j] == '+':
            if listaOperadores[j] != listaOperadores[j + 1]:
                b += 1
        else:
            if listaOperadores[j] != listaOperadores[j + 1]:
                b += 1
    mediaB = ((2 * n1 * n2) / (n1 + n2)) + 1
    varianzaB = (2 * n1 * n2 * ((2 * n1 * n2) - N)) / (N * N * (N - 1))
    Z = (b - mediaB) / (np.sqrt(varianzaB))
    # alfa = 0.05 , por lo tanto Z(1-(alfa/2)) = Z(0.025) = 1.96

    if abs(Z) < 1.96:
        print("Test aprobado. Se demuestra la Independecia, por lo tanto, la aleatoriedad también")
        print("")
        return True
    else:
        print("Test desaprobado. Se rechaza la independencia")
        print("")
        return False