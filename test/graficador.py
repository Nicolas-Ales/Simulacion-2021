import matplotlib.pyplot as plt
import numpy as np


class Graficadores:
    def graficarUniforme(self, u):
        plt.title("uniforme")
        plt.hist(u)
        plt.show()

    def graficarGamma(self, g):
        plt.title("gamma")
        plt.hist(g, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='r')
        plt.show()

    def graficarExponencial(self, e):
        plt.title("exponencial")
        plt.hist(e, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='g')
        plt.show()

    def graficarNormal(self, n):
        plt.title("normal")
        plt.hist(n, 25, histtype="stepfilled",
                 alpha=.7, linewidth=5, color='y')
        plt.show()

    def graficarPascal(self, p):
        plt.title("pascal")
        plt.bar(p, np.arange(0, 1000), width=0.1, color='r')
        plt.show()

    def graficarBinomial(self, b):
        plt.title("binomial")
        plt.bar(b, np.arange(0, 1000), width=0.5, color='r')
        plt.show()

    def graficarPoisson(self, po):
        plt.title("poisson")
        plt.bar(po, np.arange(0, 1000), width=0.5, color='r')
        plt.show()

    def graficarEmpirica(self, em):
        plt.title("empírica discreta")
        plt.bar(em, np.arange(0, 1000), width=0.5, color='r')
        plt.show()

    def graficarHipergeo(self, hip):
        plt.title("hipergeométrica")
        plt.bar(hip, np.arange(0, 1000), width=0.5, color='r')
        plt.show()