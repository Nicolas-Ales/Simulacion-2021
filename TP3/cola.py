import simpy
import numpy as np

lam = 3.0
mu = 4.0


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


wait_t = []
t_in_sistem = []


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


obs_time = []
q_length = []
usage = []
u_sistem = []


def observe(env, servers):
    while True:
        obs_time.append(env.now)
        q_length.append(len(servers.queue))
        usage.append(servers.count)
        u_sistem.append(servers.count + len(servers.queue))
        yield env.timeout(0.5)


# np.random.seed(0) #TO DO cambiar esto en la vercion final

env = simpy.Environment()
servers = simpy.Resource(env, capacity=1)
env.process(cafe_run(env, servers))
env.process(observe(env, servers))
env.run(until=1000)

f = open("metricas_lamnda_{}_mu_{}.txt".format(lam,mu), "w")
f.write('Lamnda = {} \t Mu = {}\n'.format(lam,mu))
f.write('Utilización de servidor: {:.8f}%\n'.format(np.mean(usage) * 100))
f.write('Promedio Usuarios en el sistema: {:.8f}\n'.format(np.mean(u_sistem)))
f.write('Promedio Usuarios en cola: {:.8f}\n'.format(np.mean(q_length)))
f.write('Tiempo promedio en el sistema: {:.8f}\n'.format(np.mean(t_in_sistem)))
f.write('Tiempo promedio en de espera: {:.8f}\n'.format(np.mean(wait_t)))
f.write('probabilidad de n clientes en cola:\n')
f.write('\t 1 cliente en cola: {:.4f}\n'.format(q_length.count(1) / len(q_length)))
f.write('\t 2 clientes en cola: {:.4f}\n'.format(q_length.count(2) / len(q_length)))
f.write('\t 3 clientes en cola: {:.4f}\n'.format(q_length.count(3) / len(q_length)))
f.write('\t 4 clientes en cola: {:.4f}\n'.format(q_length.count(4) / len(q_length)))
f.write('\t 5 clientes en cola: {:.4f}\n'.format(q_length.count(5) / len(q_length)))
more_than_6 = [i for i in q_length if i > 6]
f.write('\t 6 clientes en cola: {:.4f}\n'.format(len(more_than_6)/ len(q_length)))
f.write('probabilidad de denegación de servicio con una cola finita de\n')
more_than_0 = [i for i in q_length if i > 0]
f.write('\t 0 clientes: {:.4f}\n'.format(len(more_than_0)/ len(q_length)))
more_than_2 = [i for i in q_length if i > 2]
f.write('\t 2 clientes: {:.4f}\n'.format(len(more_than_2)/ len(q_length)))
more_than_5 = [i for i in q_length if i > 5]
f.write('\t 5 clientes: {:.4f}\n'.format(len(more_than_5)/ len(q_length)))
more_than_10 = [i for i in q_length if i > 10]
f.write('\t 10 clientes: {:.4f}\n'.format(len(more_than_10)/ len(q_length)))
more_than_50 = [i for i in q_length if i > 50]
f.write('\t 50 clientes: {:.4f}\n'.format(len(more_than_50)/ len(q_length)))

f.close()
f = open("metricas_lamnda_{}_mu_{}.txt".format(lam,mu), "r")
print(f.read())

import matplotlib.pyplot as plt

plt.figure()
plt.hist(wait_t)
plt.title('distribucion de los tiempos de espera')
plt.xlabel('Waiting time (min)')
plt.ylabel('number of customers')

plt.figure()
plt.hist(t_in_sistem)
plt.title('distribucion de los tiempos en el sistema')
plt.xlabel('Waiting time (min)')
plt.ylabel('number of customers')

plt.figure()
plt.step(obs_time, q_length, where='post')
plt.title('personas en la cola')

plt.figure()
plt.hist(q_length)
plt.title('probabilidad de n personas en la cola')

plt.show()
