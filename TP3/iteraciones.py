import simpy
import numpy as np
from matplotlib.ticker import PercentFormatter

iteraciones = 10
lam = 2.5
mu = 2


def generate_interarrival():
    return np.random.exponential(1. / lam)


def generate_service():
    return np.random.exponential(1. / mu)


def cafe_run(env, servers):
    i = 0
    while True:
        i += 1
        yield env.timeout(generate_interarrival())
        env.process(customer(env, i, servers))


def customer(env, customer, servers):
    with servers.request() as request:
        t_arrival = env.now
        print(env.now, 'customer {} arrives'.format(customer))
        yield request
        print(env.now, 'customer {} is being served'.format(customer))
        t_request = env.now
        yield env.timeout(generate_service())
        print(env.now, 'customer {} departs'.format(customer))
        t_depart = env.now
        wait_t.append(t_request - t_arrival)
        t_in_sistem.append(t_depart - t_arrival)


def observe(env, servers):
    while True:
        obs_time.append(env.now)
        q_length.append(len(servers.queue))
        usage.append(servers.count)
        u_sistem.append(servers.count + len(servers.queue))
        yield env.timeout(0.5)


tiemposDeEspera = []
tiemposEnSistema = []
tiempoDeObservacion = []
Uso = []
UsuariosEnCola = []
usuariosEnSistema = []

for k in range(iteraciones):
    wait_t = []
    t_in_sistem = []
    obs_time = []
    q_length = []
    usage = []
    u_sistem = []

    env = simpy.Environment()
    servers = simpy.Resource(env, capacity=1)
    env.process(cafe_run(env, servers))
    env.process(observe(env, servers))
    env.run(until=1000)

    tiemposDeEspera.append(wait_t)
    tiemposEnSistema.append(t_in_sistem)
    tiempoDeObservacion.append(obs_time)
    Uso.append(usage)
    UsuariosEnCola.append(q_length)
    usuariosEnSistema.append(u_sistem)


promedioUtilizacion = np.mean([np.mean(a) for a in Uso])
promedioUsuariosEnSistema = np.mean([np.mean(a) for a in usuariosEnSistema])
promedioUsuariosEnCola = np.mean([np.mean(a) for a in UsuariosEnCola])
promedioTiempoDeEspera = np.mean([np.mean(a) for a in tiemposDeEspera])
promedioTiempoEnSistema = np.mean([np.mean(a) for a in tiemposEnSistema])

promProbClienteEnCola0 = np.mean([a.count(0) / len(a) for a in UsuariosEnCola])
promProbClienteEnCola1 = np.mean([a.count(1) / len(a) for a in UsuariosEnCola])
promProbClienteEnCola2 = np.mean([a.count(2) / len(a) for a in UsuariosEnCola])
promProbClienteEnCola3 = np.mean([a.count(3) / len(a) for a in UsuariosEnCola])
promProbClienteEnCola4 = np.mean([a.count(4) / len(a) for a in UsuariosEnCola])
promProbClienteEnCola5 = np.mean([a.count(5) / len(a) for a in UsuariosEnCola])
promProbClienteEnCola6 = np.mean([len([i for i in a if i > 6]) / len(a) for a in UsuariosEnCola])

promProbDenegarEnCola0 = np.mean([len([i for i in a if i > 0]) / len(a) for a in UsuariosEnCola])
promProbDenegarEnCola2 = np.mean([len([i for i in a if i > 2]) / len(a) for a in UsuariosEnCola])
promProbDenegarEnCola5 = np.mean([len([i for i in a if i > 5]) / len(a) for a in UsuariosEnCola])
promProbDenegarEnCola10 = np.mean([len([i for i in a if i > 10]) / len(a) for a in UsuariosEnCola])
promProbDenegarEnCola50 = np.mean([len([i for i in a if i > 50]) / len(a) for a in UsuariosEnCola])


f = open("metricas_lamnda_{}_mu_{}.txt".format(lam, mu), "w")
f.write('Lamnda = {} \t Mu = {}\n'.format(lam, mu))
f.write('\\begin{itemize}\n')
f.write('\t\item Utilización de servidor: {:.8f}%\n'.format(promedioUtilizacion* 100))
f.write('\t\itemPromedio Usuarios en el sistema: {:.8f}\n'.format(promedioUsuariosEnSistema))
f.write('\t\itemPromedio Usuarios en cola: {:.8f}\n'.format(promedioUsuariosEnCola))
f.write('\t\itemTiempo promedio en el sistema: {:.8f}\n'.format(promedioTiempoEnSistema))
f.write('\t\itemTiempo promedio en de espera: {:.8f}\n'.format(promedioTiempoDeEspera))
f.write('\t\item probabilidad de n clientes en cola:\n')
f.write('\t\\begin{itemize}\n')
f.write('\t\t\item 0 clientes en cola: {:.4f}\n'.format(promProbClienteEnCola0))
f.write('\t\t\item 1 cliente en cola: {:.4f}\n'.format(promProbClienteEnCola1))
f.write('\t\t\item 2 clientes en cola: {:.4f}\n'.format(promProbClienteEnCola2))
f.write('\t\t\item 3 clientes en cola: {:.4f}\n'.format(promProbClienteEnCola3))
f.write('\t\t\item 4 clientes en cola: {:.4f}\n'.format(promProbClienteEnCola4))
f.write('\t\t\item 5 clientes en cola: {:.4f}\n'.format(promProbClienteEnCola5))
f.write('\t\t\item 6 clientes en cola: {:.4f}\n'.format(promProbClienteEnCola6))
f.write('\t\end{itemize}\n')
f.write('\t\item probabilidad de denegación de servicio con una cola finita de\n')
f.write('\t\\begin{itemize}\n')
f.write('\t\t\item 0 clientes: {:.4f}\n'.format(promProbDenegarEnCola0))
f.write('\t\t\item 2 clientes: {:.4f}\n'.format(promProbDenegarEnCola2))
f.write('\t\t\item 5 clientes: {:.4f}\n'.format(promProbDenegarEnCola5))
f.write('\t\t\item 10 clientes: {:.4f}\n'.format(promProbDenegarEnCola10))
f.write('\t\t\item 50 clientes: {:.4f}\n'.format(promProbDenegarEnCola50))
f.write('\t \end{itemize}')
f.write('\n\end{itemize}')

f.close()
f = open("metricas_lamnda_{}_mu_{}.txt".format(lam, mu), "r")
print(f.read())

import matplotlib.pyplot as plt
import matplotlib.pylab as pl

colors = pl.cm.jet(np.linspace(0,1,10))

tiemposDeEsperaTotales = []
for a in tiemposDeEspera:
    tiemposDeEsperaTotales.extend(a)
fig1, (TE, TS) = plt.subplots(ncols=2, sharey=True)
fig1.set_figheight(4)
fig1.set_figwidth(8)
fig1.subplots_adjust(bottom=0.13, top=0.85, left=0.14,wspace=0.07)

TE.hist(tiemposDeEsperaTotales)
TE.set_title('distribucion de los tiempos\n de espera')
TE.set_xlabel('Tiempo de Espera (min)')
TE.set_ylabel('Numero de clientes')
TE.set_xlim(0)

tiemposEnSistemaTotales = []
for a in tiemposEnSistema:
    tiemposEnSistemaTotales.extend(a)

TS.hist(tiemposEnSistemaTotales)
TS.set_title('distribucion de los tiempos\n en el sistema')
TS.set_xlabel('Tiempo de Espera (min)')
TS.set_xlim(0)

fig1.savefig('distribuciones lamnda {} mu {}.png'.format(lam, mu))

fig2, QL = plt.subplots(1)
fig2.set_figheight(4)
fig2.set_figwidth(8)
fig2.subplots_adjust(left=0.07,right=0.80,bottom=0.13)
for i,q in enumerate(UsuariosEnCola):
    QL.step(obs_time, q,label='Iteracion {}'.format(i),where='post',color=colors[i],linewidth=0.5)
QL.set_title('Personas en la Cola')
QL.set_xlim(0,500)
QL.set_ylim(0)
QL.set_xlabel('Tiempo (min)')
QL.set_ylabel('Personas en cola')
fig2.legend(loc='center right')
fig2.savefig('Personas en cola lamnda {} mu {}.png'.format(lam, mu))

probTotales = []
for a in UsuariosEnCola:
    probTotales.extend(a)

fig3, PPC = plt.subplots(1)
labels, counts = np.unique(probTotales, return_counts=True)
percent = [a/len(probTotales) for a in counts]
PPC.bar(labels,percent,align='center')
# plt.hist(probTotales,bins=20,orientation='horizontal',weights=np.ones(len(probTotales)) / len(probTotales),rwidth=0.9,align='left')
PPC.yaxis.set_major_formatter(PercentFormatter(1))
PPC.set_xlim(xmin=-0.5,xmax=20)
PPC.set_xticks(range(20))
PPC.set_title('Probabilidad de n personas en la cola')
fig3.savefig('Probabilidades de n personas en cola lamnda {} mu {}.png'.format(lam, mu))

plt.show()
