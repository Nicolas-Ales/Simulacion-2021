import simpy
import numpy as np

min_demanda = 1
max_demanda = 5             # intervalo de valores enteros que puede tomar la demanda (distribucion uniforme)
parametro_arribos = 5       # lamda de la distribucion exponencial de arribos de clientes

min_inventario = 50         # s: cantidad minima deseable de inventario
max_inventario = 200        # S: cantidad maxima de unidades en inventario
dias_entre_pedidos = 15     # Cada cuanto se hace un pedido
cOrden = 80                 # Costo por ordenar una unidad
cFaltante = 50              # Costo por unidad de no poder satisfacer la demanda requerida
cMantenimiento = 5          # Costo de mantener en deposito una unidad
valor_unidad = 100          # Valor al que se vende cada unidad


def simulacion_inventario(env, min_inventario, max_inventario):
    global inventario, balance, cant_ordenada, costo_de_faltante, costo_de_orden, costo_de_mantenimiento
    inventario = max_inventario
    balance = 0.0
    cant_ordenada = 0
    costo_de_faltante = 0
    costo_de_orden = 0
    costo_de_mantenimiento = 0

    while True:
        tiempo_entre_arribo = generate_interarrival()
        yield env.timeout(tiempo_entre_arribo)
        demanda = generate_demand()
        if demanda < inventario:
            balance += valor_unidad * demanda
            inventario -= demanda
            print('{:.2f} vendido {}'.format(env.now, demanda))
        else:
            balance += 100 * inventario
            costo_de_faltante -= cFaltante * (inventario - demanda)
            inventario = 0
            print('{:.2f} vendido {} (sin stock)'.format(env.now, inventario))


def orden(env):
    global inventario, min_inventario, max_inventario
    while True:
        env.process(hacer_orden(env, max_inventario))
        yield env.timeout(dias_entre_pedidos)


def hacer_orden(env, order_target):
    global inventario, cant_ordenada, costo_de_orden

    cant_ordenada = order_target - inventario
    print('{:.2f} orden hecha por {}'.format(env.now, cant_ordenada))
    costo_de_orden += cOrden * cant_ordenada
    yield env.timeout(2.0)
    inventario += cant_ordenada
    cant_ordenada = 0
    print('{:.2f} orden recibida, {} en inventario'.format(env.now, inventario))


def generate_interarrival():
    return np.random.exponential(1. / parametro_arribos)


def generate_demand():
    return np.random.randint(min_demanda,max_demanda)


obs_time = []
inventory_level = []
balance_time = []
costoF = []
costoO = []
costoM = []


def observe(env):
    global inventario, balance, costo_de_faltante, costo_de_orden, costo_de_mantenimiento
    while True:
        costo_de_mantenimiento += 0.1 * cMantenimiento * inventario
        obs_time.append(env.now)
        inventory_level.append(inventario)
        balance_time.append(balance)
        costoF.append(costo_de_faltante)
        costoO.append(costo_de_orden)
        costoM.append(costo_de_mantenimiento)
        yield env.timeout(0.1)


np.random.seed(0)
env = simpy.Environment()
env.process(simulacion_inventario(env, min_inventario, max_inventario))
env.process(orden(env))
env.process(observe(env))
env.run(until=90.0)

costoTotal = []
balanceTotal = []
for i, _ in enumerate(obs_time):
    costo_total = costoF[i] + costoO[i] + costoM[i]
    costoTotal.append(costo_total)
    balance_total = balance_time[i] - costo_total
    balanceTotal.append(balance_total)

balancePos = []
balanceNeg = []

aux = True
for b in balanceTotal:
    if b >= 0 and aux == True:
        balancePos.append(b)
        balanceNeg.append(np.nan)
        aux = True
    elif b >= 0 and aux == False:
        balancePos.append(b)
        balanceNeg.append(b)
        aux = False
    elif b < 0 and aux == True:
        balancePos.append(b)
        balanceNeg.append(b)
        aux = False
    elif b < 0 and aux == False:
        balancePos.append(np.nan)
        balanceNeg.append(b)

import matplotlib.pyplot as plt

fig1, (InvL, BlnT, CF, CO, CM) = plt.subplots(5, sharex=True)

InvL.step(obs_time, inventory_level, where='post')
InvL.set(xlabel='Simulation Time (days)', ylabel='Inventory level')
InvL.label_outer()
InvL.set_xlim(xmin=0)
InvL.set_ylim(ymin=0)

BlnT.step(obs_time, balance_time, where='post', color='green')
BlnT.set(xlabel='Simulation Time (days)', ylabel='Balance')
BlnT.label_outer()
BlnT.set_xlim(xmin=0)
BlnT.set_ylim(ymin=0)

CF.step(obs_time, costoF, where='post', color='red')
CF.set(xlabel='Simulation Time (days)', ylabel='Costo Faltante')
CF.label_outer()
CF.set_xlim(xmin=0)

CO.step(obs_time, costoO, where='post', color='red')
CO.set(xlabel='Simulation Time (days)', ylabel='Costo Orden')
CO.label_outer()
CO.set_xlim(xmin=0)

CM.step(obs_time, costoM, where='post', color='red')
CM.set(xlabel='Simulation Time (days)', ylabel='Costo Mantenimiento')
CM.label_outer()
CM.set_xlim(xmin=0)

fig2, (CT, Bal) = plt.subplots(2, sharex=True)

CT.step(obs_time, costoTotal, where='post', color='red')
CT.set(xlabel='Simulation Time (days)', ylabel='Costos Totales')
CT.label_outer()
CT.set_xlim(xmin=0)

Bal.step(obs_time, balanceNeg, where='post', color='red')
plt.axhline(0, color='black')
Bal.step(obs_time, balancePos, where='post', color='green')
Bal.set(xlabel='Simulation Time (days)', ylabel='Balance')
Bal.label_outer()
Bal.set_xlim(xmin=0)

plt.show()
