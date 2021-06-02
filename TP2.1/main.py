import generadores
import pruebas
import graficos

def ejecuta_pruebas(muestra):
    print('Prueba Kolmogorov-Smirnov')
    pruebas.pruebaKS(muestra)
    print('Prueba de Paridad')
    pruebas.pruebaParidad(muestra)
    print('Prueba Chi Cuadrado')
    pruebas.pruebaChiCuadrado(muestra)
    print('Prueba de Rachas')
    pruebas.pruebaRachas(muestra)

n = 240000 #cantidad de muestras
seed = 5789 #Seed para los generadores

muestraGLC = generadores.generadorGCL(seed,678954113, 1, 2 ** 32,n)
print('Generador GCL','\n numeros de muestras: ',n,'\n seed = ',seed)
ejecuta_pruebas(muestraGLC)
graficos.grafRuido(muestraGLC,'GLC')
graficos.grafPar(muestraGLC,'GLC')
graficos.grafHist(muestraGLC,'GLC')

muestraMedia= generadores.generadorMediaCuadrados(1964,n)
ejecuta_pruebas(muestraMedia)
graficos.grafRuido(muestraMedia,'Cuadrados')
graficos.grafPar(muestraMedia,'Cuadrados')
graficos.grafHist(muestraMedia,'Cuadrados')

muestraNunPy= generadores.generadorNunPy(seed,n)
ejecuta_pruebas(muestraNunPy)
graficos.grafRuido(muestraNunPy,'NunPy')
graficos.grafPar(muestraNunPy,'NunPy')
graficos.grafHist(muestraNunPy,'NunPy')