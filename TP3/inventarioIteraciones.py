import simpy
import numpy as np

iteraciones = 100

min_demanda = 1
max_demanda = 5             # intervalo de valores enteros que puede tomar la demanda (distribucion uniforme)
parametro_arribos = 5       # lamda de la distribucion exponencial de arribos de clientes

min_inventario = 50         # s: cantidad minima deseable de inventario
max_inventario = 200        # S: cantidad maxima de unidades en inventario
dias_entre_pedidos = 15     # Cada cuanto se hace un pedido
cOrden = 50                 # Costo por ordenar una unidad
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
        if inventario < min_inventario:
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


obs_time_IT = []
inventory_level_IT = []
balance_time_IT = []
costoF_IT = []
costoO_IT = []
costoM_IT = []
costoTotal_IT = []
balanceTotal_IT = []

for k in range(iteraciones):
    obs_time = []
    inventory_level = []
    balance_time = []
    costoF = []
    costoO = []
    costoM = []

    # np.random.seed(0)
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

    obs_time_IT.append(obs_time)
    inventory_level_IT.append(inventory_level)
    balance_time_IT.append(balance_time)
    costoF_IT.append(costoF)
    costoO_IT.append(costoO)
    costoM_IT.append(costoM)
    costoTotal_IT.append(costoTotal)
    balanceTotal_IT.append(balanceTotal)

import matplotlib.pyplot as plt
import matplotlib.pylab as pl

colorsInv = pl.cm.copper(np.linspace(0,5,900))
colorsCost = pl.cm.Reds(np.linspace(0,10,900))
colorsGain = pl.cm.Greens(np.linspace(0,10,900))
colorsBalance = pl.cm.Spectral(np.linspace(0,8,900))



plt.style.use('seaborn-paper')
fig1, InvL = plt.subplots(1, sharex=True)
fig1.set_figheight(2.3)
fig1.set_figwidth(6)
fig1.subplots_adjust(bottom=0.21, top=0.99, left=0.14)

for i in range(len(obs_time_IT)):
    InvL.step(obs_time_IT[i], inventory_level_IT[i], where='post',color=colorsInv[i])
InvL.set(xlabel='Tiempo de Simulación (Días)', ylabel='Unidades en Inventario')
InvL.label_outer()
InvL.set_xlim(xmin=0)
InvL.set_ylim(ymin=0)
fig1.savefig('Nivel Inventario')

fig2, (BlnT, CF, CO, CM) = plt.subplots(4, sharex=True)
fig2.set_figheight(5)
fig2.set_figwidth(6)
fig2.subplots_adjust(bottom=0.10, top=0.99, left=0.14, hspace=0.07)

for i in range(len(obs_time_IT)):
    BlnT.step(obs_time_IT[i], balance_time_IT[i], where='post', color=colorsGain[i])
BlnT.set(xlabel='Tiempo de Simulación (Días)', ylabel='Ingreso')
BlnT.label_outer()
BlnT.set_xlim(xmin=0)
BlnT.set_ylim(ymin=0)

for i in range(len(obs_time_IT)):
    CF.step(obs_time_IT[i], costoF_IT[i], where='post', color=colorsCost[i])
CF.set(xlabel='Tiempo de Simulación (Días)', ylabel='Costo Faltante')
CF.label_outer()
CF.set_xlim(xmin=0)

for i in range(len(obs_time_IT)):
    CO.step(obs_time_IT[i], costoO_IT[i], where='post', color=colorsCost[i])
CO.set(xlabel='Tiempo de Simulación (Días)', ylabel='Costo Orden')
CO.label_outer()
CO.set_xlim(xmin=0)

for i in range(len(obs_time_IT)):
    CM.step(obs_time_IT[i], costoM_IT[i], where='post', color=colorsCost[i])
CM.set(xlabel='Tiempo de Simulación (Días)', ylabel='Costo \nMantenimiento')
CM.label_outer()
CM.set_xlim(xmin=0)

fig2.savefig('Ingreso Costos')

fig3, (CT, Bal) = plt.subplots(2, sharex=True)
fig3.set_figheight(3)
fig3.set_figwidth(6)
fig3.subplots_adjust(bottom=0.21, top=0.99, left=0.14, hspace=0.07)
for i in range(len(obs_time_IT)):
    CT.step(obs_time_IT[i], costoTotal_IT[i], where='post', color=colorsCost[i])
CT.set(xlabel='Tiempo de Simulación (Días)', ylabel='Costos Totales')
CT.label_outer()
CT.set_xlim(xmin=0)

# Bal.step(obs_time, balanceNeg, where='post', color='red')
for i in range(len(obs_time_IT)):
    Bal.step(obs_time_IT[i], balanceTotal_IT[i], where='post',color=colorsBalance[i])
plt.axhline(0, color='black')
# Bal.step(obs_time, balancePos, where='post', color='green')
Bal.set(xlabel='Tiempo de Simulación (Días)', ylabel='Balance')
Bal.label_outer()
Bal.set_xlim(xmin=0)

fig3.savefig('Balance')

plt.show()

CosT =[]
for cT in costoTotal_IT:
    CosT.append(cT.pop())
BalT =[]
for bT in balanceTotal_IT:
    BalT.append(bT.pop())

print('Balance total: {}'.format(np.mean(BalT)))
print('Costo total: {}'.format(np.mean(CosT)))

