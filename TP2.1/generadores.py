from graficos import grafRuido
import random
import numpy as np


def generadorGCL(seed, a, c, m, n):
    # a Constante multiplicativa
    # c Constante Aditiva
    # m Modulo
    numeros = []
    uniform0a1 = []
    numeros.append(seed)
    for i in range(n):
        num = ((a * numeros[i - 1]) + c) % m
        numeros.append(num)
        uniform0a1.append(num / m)
    return uniform0a1


def generadorMediaCuadrados(seed, n):
    seeds = []
    valor = []
    #seed = 45679563
    seeds.append(seed)
    for i in range(n):
        cuadrado = seeds[i] ** 2
        valor.append(cuadrado / 10 ** 8)
        semilla = int(str(seeds[i] ** 2).zfill(8)[2:6])
        seeds.append(semilla)
        # print('Iteracion ', i, '\tSeed: ', seeds[i], '\t valor: ', valor[i])
    return valor


def generadorNunPy(seed,n):
    random.seed(seed)
    numeros = []
    for _ in range(n):
        numeros.append(random.uniform(0, 1))
    return numeros

