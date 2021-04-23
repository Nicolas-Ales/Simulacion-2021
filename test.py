import random
import math
import scipy.stats as ss
from scipy.stats import norm
import matplotlib
import matplotlib.pyplot as plt

def UNIFORM (a,b):
    x=[]
    for i in range(1000):
        r = round(random.random(), 4)
        x.append(a+(b-a)*r)
    return x
def EXPENT (alfa):
    ex = 1/ alfa
    x = []
    for i in range(1000):
        r = random.random()
        x += [-ex*(math.log(r))]
    return x
def GAMMA (k,a):
    x=[]
    for i in range(1, 1000):
        tr=1.0
        for j in range(1,k):
            r = random.random()
            tr=tr*r
        x.append(-(math.log10(tr))/a)
    return x
def PASCAL(k,q):
    nx = []
    for i in range(1000):
        tr = 1
        qr = math.log10(q)
        for j in range(k):
            r = random.random()
            tr *= r
        x = int(math.log10(tr)//qr)
        nx.append(x)
    return nx
def BINOMIAL (n,p):
    x=[]
    for i in range(1000):
        y=0
        for j in range(1,n):
            r = random.random()
            if (r-p) <0:
                y+=1.0
        x.append(y)
    #print (x)
    return x
Uniforme=(UNIFORM(1,3))
Gamma=(GAMMA(3, 1))
Exponencial=(EXPENT(1))
Pascal=PASCAL(3,0.3)
Binomial = BINOMIAL (1000, 0.3)
def plotear(U, G , E , P, B):
    plt.title("Distribución Uniforme")
    plt.hist(U)
    plt.show()
    plt.title("Distribución Exponencial")
    plt.hist(E)
    plt.show()
    plt.title("Distribución Gamma")
    plt.hist(G)
    plt.show()
    plt.title("Distribución Pascal")
    plt.hist(P)
    plt.show()
    plt.title("Distribución Binomial")
    plt.hist(B)
    plt.show()

plotear(Uniforme , Exponencial , Gamma , Pascal, Binomial)
