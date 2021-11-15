import random
import numpy as np
import math


class GeneradorUniforme:
    def gen(self, a, b):
        while True:
            r = random.random()
            x = a+(b-a)*r
            yield x

    def muestra(self, a, b, n):
        sample = []
        generadorsito = self.gen(a, b)
        for i in range(n):
            observation = float(next(generadorsito))
            sample.append(observation)
        return sample


class GeneradorExponencial:
    def gen(self, ex):
        while True:
            r = random.random()
            x = -ex*(np.log(r))
            yield x

    def muestra(self, ex, n):
        sample = []
        generadorsito = self.gen(ex)
        for _ in range(n):
            sample.append(float(next(generadorsito)))
        return sample


class GeneradorNormal:
    def gen(self, STDX, EX):
        while True:
            k = 12
            sum = 0.0
            for _ in range(k):
                r = random.random()
                sum += r
            x = (STDX * ((k/12)**(1/2)) * (sum - 6.0)) + EX
            yield x

    def muestra(self, STDX, EX, n):
        sample = []
        generadorsito = self.gen(STDX, EX)
        for _ in range(n):
            sample.append(float(next(generadorsito)))
        return sample


class GeneradorGamma:
    def gen(self, k, a):
        while True:
            tr = 1.0
            for _ in range(1, k):
                r = random.random()
                tr = tr * r
            x = -np.log10(tr)/a
            yield x

    def muestra(self, k, a, n):
        sample = []
        generadorsito = self.gen(k, a)
        for _ in range(n):
            observation = float(next(generadorsito))
            sample.append(observation)
        return sample


class GeneradorPascal:
    def gen(self, k, q):
        while True:
            tr = 1
            qr = np.log10(q)
            for _ in range(1, k):
                r = random.random()
                tr = tr*r
            x = np.log10(tr)/qr
            yield x

    def muestra(self, k, q, n):
        sample = []
        generadorsito = self.gen(k, q)
        for _ in range(n):
            observation = float(next(generadorsito))
            sample.append(observation)
        return sample


class GeneradorBinomial:
    def gen(self, n, p):
        while True:
            x = 0
            for _ in range(n):
                r = random.random()
                if r <= p:
                    x = x + 1.0
            yield x

    def muestra(self, n, p, nmuestra):
        sample = []
        generadorsito = self.gen(n, p)
        for _ in range(nmuestra):
            observation = float(next(generadorsito))
            sample.append(observation)
        return sample


class GeneradorHipergeo:
    def gen(self, tn, ns, p):
        while True:
            y = 0.0
            for _ in range(1, ns):
                r = random.random()
                if(r-p) > 0:
                    s = 0.0
                else:
                    s = 1.0
                    y += 1.0
                p = (tn*p-s)/(tn-1.0)
                tn -= 1.0
            yield y

    def muestra(self, tn, ns, p, n):
        sample = []
        generadorsito = self.gen(tn, ns, p)
        for _ in range(n):
            observation = float(next(generadorsito))
            sample.append(observation)
        return sample


class GeneradorEmpirica:
    def gen(self):
        p = [0.273, 0.037, 0.195, 0.009, 0.124,
             0.058, 0.062, 0.151, 0.047, 0.044]
        while True:
            r = random.random()
            a = 0
            z = 1
            for i in p:
                a += i
                if (r <= a):
                    break
                else:
                    z += 1
            yield z

    def muestra(self, n):
        sample = []
        generadorsito = self.gen()
        for _ in range(n):
            observation = float(next(generadorsito))
            sample.append(observation)
        return sample

class GeneradorPoisson:
    def gen(self, p):
        while True:
            x = 0
            tr = 1
            b = 0
            while tr>=b:
                b = math.exp(-p)
                r = random.random()
                tr = tr * r
                if tr>=b:
                    x = x + 1
            yield x

    def muestra(self, p, n):
        sample = []
        generadorsito = self.gen(p)
        for _ in range(n):
            observation = float(next(generadorsito))
            sample.append(observation)
        return sample