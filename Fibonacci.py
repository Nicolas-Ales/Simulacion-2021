import random as rn
import matplotlib.pyplot as plt

# Apuesta con la estrategia fibonacci hasta quedarnos sin dinero
# Apostamos al rojo

iteraciones = 30
rango_max = 2000

# Parametros inciales
dinero_inicial = 10000
apuesta_minima = 100
apuesta_maxima = 5000

fibonacci = [100, 100, 200, 300, 500, 800, 1300, 2100, 3400, 5000]
#secuencia de fibonacci adaptada a nuestros parametros iniciales

# ruleta
min_n = 0
max_n = 36
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36]


# numeros_negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 22, 24, 26, 28, 30, 33, 35]  Esta de referencia nomas, no se usa

def getColor(numero):
    if numero in numeros_rojos:
        return "rojo"
    elif numero == 0:
        return "sin"
    else:
        return "negro"

def actualizaPuntero(p, tipo):  # 0 perdedor, 1 ganador
    if tipo == 0:
        if p + 1 < 10:
            return p + 1
        else:
            return 9
    elif p - 2 < 0:
        p = 0
    else:
        p -= 2
    return p

def muestraGraficas(itC, itF):
    plt.figure(figsize=(6, 3.4))
    plt.title('Dinero en caja')
    for c in itC:
        plt.plot(c)
    plt.axhline(dinero_inicial, color='red', label='dinero incial')
    plt.legend(loc="upper right")
    plt.ylabel('dinero en caja')
    plt.xlabel('n(numero de tiradas)')
    plt.xlim(xmin=0)
    plt.ylim(0)
    plt.savefig('fibonacci caja', bbox_inches="tight")
    plt.show()

    plt.figure(figsize=(6, 3.4))
    plt.title('Porcentaje de Victorias')
    for f in itF:
        plt.plot(f)
    plt.axhline(0.4865, color='red', label='frecuencia esperada')
    plt.legend(loc="upper right")
    plt.ylabel('porcentaje de victorias')
    plt.xlabel('n(numero de tiradas)')
    plt.xlim(xmin=0)
    plt.ylim(0)
    plt.savefig('fibonacci frec', bbox_inches="tight")
    plt.show()


def main():
    iteraciones_caja = []
    iteraciones_frec = []
    for i in range(iteraciones):
        lista_numeros = []
        lista_dinero = []
        lista_frec = []
        dinero = dinero_inicial
        apuesta = apuesta_minima
        puntero = 0
        count = 0
        count_victorias = 0

        while dinero >= 0:
            lista_dinero.append(dinero)
            if apuesta > dinero:
                break
            n = rn.randint(min_n, max_n)
            lista_numeros.append(n)
            if getColor(n) == "rojo":
                dinero += apuesta
                count_victorias += 1
                puntero = actualizaPuntero(puntero, 1)
            else:
                if getColor(n) == "negro":
                    dinero -= apuesta
                else:
                    dinero -= apuesta / 2
                puntero = actualizaPuntero(puntero, 0)
            count += 1
            apuesta = fibonacci[puntero]
            frecuencia = count_victorias/count
            print(frecuencia)
            lista_frec.append(frecuencia)
            if count >= rango_max:
                break
        iteraciones_caja.append(lista_dinero)
        iteraciones_frec.append(lista_frec)
    muestraGraficas(iteraciones_caja, iteraciones_frec)


main()
