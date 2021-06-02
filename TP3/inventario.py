import simpy
import numpy as np


def warehouse_run(env, order_cutoff, order_target):
    global inventory, balance, num_ordered
    inventory = order_target
    balance = 0.0
    num_ordered = 0

    while True:
        interarrival = generate_interarrival()
        yield env.timeout(interarrival)
        balance -= inventory * 2 * interarrival
        demand = generate_demand()
        if demand < inventory:
            balance += 100 * demand
            inventory -= demand
            print('{:.2f} sold {}'.format(env.now, demand))
        else:
            balance += 100 * inventory
            inventory = 0
            print('{:.2f} sold {} (out of stock)'.format(env.now, inventory))

        if inventory < order_cutoff and num_ordered == 0:
            env.process(handle_order(env, order_target))

def handle_order(env, order_target):
    global inventory, balance, num_ordered

    num_ordered = order_target - inventory
    print('{:.2f} placed order for {}'.format(env.now, num_ordered))
    balance -= 50*num_ordered
    yield env.timeout(2.0)
    inventory += num_ordered
    num_ordered = 0
    print('{:.2f} received order, {} in inventory'.format(env.now, inventory))


def generate_interarrival():
    return np.random.exponential(1. / 5)


def generate_demand():
    return np.random.randint(1, 5)

obs_time = []
inventory_level = []
balance_time = []

def observe(env):
    global inventory, balance
    while True:
        obs_time.append(env.now)
        inventory_level.append(inventory)
        balance_time.append(balance)
        yield env.timeout(0.1)

np.random.seed(0)
env = simpy.Environment()
env.process(warehouse_run(env, 30, 50))
env.process(observe(env))
env.run(until=30.0)

import matplotlib.pyplot as plt

fig, (InvL,BlnT)= plt.subplots(2,sharex=True)

InvL.step(obs_time,inventory_level,where='post')
InvL.set(xlabel='Simulation Time (days)',ylabel='Inventory level' )
InvL.label_outer()
InvL.set_xlim(xmin=0)
InvL.set_ylim(ymin=0)

BlnT.step(obs_time,balance_time,where='post')
BlnT.set(xlabel='Simulation Time (days)',ylabel='Balance' )
BlnT.label_outer()
BlnT.set_xlim(xmin=0)
BlnT.set_ylim(ymin=0)


plt.show()
