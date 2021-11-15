from os import system, name
from generadores import *
from graficador import Graficadores

from tests import *

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    clearScreen()
    muestraUniforme = GeneradorUniforme().muestra(1, 3, 1000)
    muestraExponencial = GeneradorExponencial().muestra(5, 1000)
    muestraNormal = GeneradorNormal().muestra(30, 2.35, 1000)
    muestraGamma = GeneradorGamma().muestra(5,20, 1000)
    muestraPascal = GeneradorPascal().muestra(5,0.5,1000)
    muestraBinomial = GeneradorBinomial().muestra(1000,0.4,1000)
    muestraPoisson = GeneradorPoisson().muestra(50, 1000)
    muestraEmpirica = GeneradorEmpirica().muestra(1000)
    muestraHipergeo = GeneradorHipergeo().muestra(5000000,500,0.4, 1000)
    # tests
    squareChiUniform(muestraUniforme)
    squareChiExponential(muestraExponencial)
    squareChiNormal(muestraNormal)
    squareChiBinomial(muestraBinomial)
    squareChiPoisson(muestraPoisson)
    squeareChiEmpirica(muestraEmpirica)
    # graficos
    gfx = Graficadores()
    gfx.graficarUniforme(muestraUniforme)
    gfx.graficarExponencial(muestraExponencial)
    gfx.graficarNormal(muestraNormal)
    gfx.graficarGamma(muestraGamma)
    gfx.graficarBinomial(muestraBinomial)
    gfx.graficarPascal(muestraPascal)
    gfx.graficarPoisson(muestraPoisson)
    gfx.graficarEmpirica(muestraEmpirica)
    gfx.graficarHipergeo(muestraHipergeo)