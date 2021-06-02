import random
import math


def r():
    return random.uniform(0, 1)

def randomUniforme(a, b):
    return r() * (b - a) + a


def randomExponencial(lamb):
    return -(1 / lamb) * (math.log(r()))


def randomGamma(alpha, k):
    tr = 1.0
    for _ in range(0, k):
        tr *= r()
    return -(1 / alpha) * math.log(tr)


def randomNormal(mu, sigma, k):
    sum = 0
    for _ in range(0, k):
        sum += r()
    return sigma * math.sqrt((12 / k)) * (sum - (k / 2)) + mu


def randomPascal(k, q):
    multiplier = 1
    for _ in range(0, k):
        multiplier *= r()
    x = math.log(multiplier) / math.log(q)
    return math.floor(x)


def randomBinomial(n, p):
    x = 0
    for _ in range(0, n):
        if (r() - p) <= 0:
            x += 1
    return x


def randomHipergeometrica(N, n, p):
    x = 0.0
    for _ in range(1, n):
        R = r()
        if (R - p) <= 0:
            s = 1
            x += 1
        else:
            s = 0
        p = (N * p - s) / (N - 1)
        N -= 1
    return x


def randomPoisson(lamb):
        x = 0
        tr = 1
        b = 0
        while tr >= b:
            b = math.exp(-lamb)
            tr *= r()
            if tr>=b:
                x+=1
            else:
                break
        return x


def randomEmpirica():
    p = [0.143, 0.037, 0.186, 0.018, 0.234, 0.078, 0.144, 0.061, 0.047, 0.052]
    R = r()
    acum = 0
    x = 1
    for i in p:
        acum += i
        if R < acum:
            break
        else:
            x += 1
    return x