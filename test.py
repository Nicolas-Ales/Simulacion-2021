import numpy as np
import matplotlib.pyplot as plt


class Data(object):
    def __init__(self, r=0, i=0):
        self.time = None

        self.serverStatus = None
        self.numInQ = None
        self.timeLastEvent = None

        self.numcustsDelayed = None
        self.totalOfDelays = None
        self.areaNumInQ = None
        self.areaNumInSystem = None
        self.areaServerStatus = None

        self.timeNextEvent = [0, 0]

        self.timeArrival = []

        self.interarrival_rate = None
        self.service_rate = None
        self.numDelaysRequired = None

        self.numEvents = None
        self.qLimit = None

        self.nextEventType = None

        #---------------------
        self.timeInQList = []
        self.timeInSystemList = []
        self.numInQList = []
        self.numInSystemList = []
        self.serverStatusAvgList = []

        self.totalOfDelaysSystem = 0
        self.iteration = 0
        #---------------------

def initialize(d):
    d.time = 0
    # Initialize the state variables.
    d.serverStatus = 0
    d.numInQ = 0
    d.timeLastEvent = 0.0

    # Initialize the statistical counters.
    d.numcustsDelayed = 0
    d.totalOfDelays = 0.0
    d.areaNumInQ = 0.0
    d.areaNumInSystem = 0.0
    d.areaServerStatus = 0.0

    # Initialize event list. Since no customers are present, the departure (service completion) event is eliminated from consideration.
    d.timeNextEvent[0] = d.time + np.random.exponential(1.0 / d.interarrival_rate)
    d.timeNextEvent[1] = 1.0E+30


def timing(d):
    minTimeNextEvent = 1.0E+29
    d.nextEventType = -1

    # Determine the event type of the next event to occur.
    for i in range(0, d.numEvents):
        if d.timeNextEvent[i] < minTimeNextEvent:
            minTimeNextEvent = d.timeNextEvent[i]
            d.nextEventType = i

    # Check to see whether the event list is empty.
    if d.nextEventType == -1:
        print('event list empty at time ' + str(d.time))
        exit()

    # The event list is not empty, so advance the simulation clock.
    d.time = minTimeNextEvent


def arrive(d):
    # Schedule next arrival.
    d.timeNextEvent[0] = d.time + np.random.exponential(1.0 / d.interarrival_rate)

    # Check to see whether server is busy
    if d.serverStatus == 1:
        # Server is busy, so increment number of customers in queue.
        d.numInQ = d.numInQ + 1
        # Check to see whether an overflow condition exists.
        if d.numInQ >= d.qLimit:
            # The queue has overflowed, so'stop the simulation.
            print('Overflow of the array timeArrival at time ' + str(d.time))
            exit()
        # There is still room in the queue, so store the time of arrival of the arriving' customer at the (new) end of timeArrival.
        d.timeArrival[d.numInQ-1] = d.time

    else:
        # Server is idle, so arriving customer has a delay of zero. Increment the number of customers delayed, and make server busy.
        d.timeInQList.append(0)
        d.numcustsDelayed = d.numcustsDelayed + 1
        d.serverStatus = 1
        # Schedule a departure (service completion).
        d.timeNextEvent[1] = d.time + np.random.exponential(1.0 / d.service_rate)
        fullDelay = d.timeNextEvent[1] -d.time
        d.timeInSystemList.append(fullDelay)
        d.totalOfDelaysSystem = d.totalOfDelaysSystem + fullDelay


def depart(d):
    # Check to see whether the queue is empty.
    if d.numInQ == 0:
        # The queue is empty so make the server idle and eliminate the departure (service completion) event from consideration.
        d.serverStatus = 0
        d.timeNextEvent[1] = 1.0E+30
    else:
        # The queue is nonempty, so decrement the number of customers in queue.
        d.numInQ = d.numInQ - 1
        # compute the delay of the customer who is beginning service and update the,total delay accumulator.
        delay = d.time - d.timeArrival[0]
        d.timeInQList.append(delay)
        d.totalOfDelays = d.totalOfDelays + delay
        # Increment the number of customers delayed, and schedule departure.
        d.numcustsDelayed = d.numcustsDelayed + 1
        d.timeNextEvent[1] = d.time + np.random.exponential(1.0 / d.service_rate)
        fullDelay = d.timeNextEvent[1] - d.timeArrival[0]
        d.timeInSystemList.append(fullDelay)
        d.totalOfDelaysSystem = d.totalOfDelaysSystem + fullDelay
        # Move each customer in queue (if any) up one place.
        for i in range(0, d.numInQ):
            d.timeArrival[i] = d.timeArrival[i + 1]


def report(d):
    avgDelayInQ = d.totalOfDelays / d.numcustsDelayed
    avgDelayInSystem = d.totalOfDelaysSystem / d.numcustsDelayed
    avgNumInQ = d.areaNumInQ / d.time
    avgNumInSystem = d.areaNumInSystem / d.time
    serverUtilization = d.areaServerStatus / d.time
    print("")
    print("Experimento número "+ str(d.iteration))
    print("")
    print("Promedio de demora en el sistema: " + str(avgDelayInSystem))
    print("")
    print("Promedio de demora en la cola: " + str(avgDelayInQ))
    print("")
    print("promedio de clientes en la cola: " + str(avgNumInQ))
    print("")
    print("promedio de clientes en el sistema: " + str(avgNumInSystem))
    print("")
    print("Utilización del servidor: " + str(serverUtilization))
    print("")
    print("Tiempo de finalización de la simulación: " + str(d.time))
    print("")

def updateTimeAvgStats(d):
    # Compute time since last event, and marker
    timeSinceLastEvent = d.time - d.timeLastEvent

    d.numInQList[d.numInQ]  = d.numInQList[d.numInQ] + timeSinceLastEvent
    d.numInSystemList[d.numInQ + d.serverStatus] = d.numInSystemList[d.numInQ + d.serverStatus] + timeSinceLastEvent

    d.timeLastEvent = d.time
    # Update area under number-in-queue function.
    d.areaNumInQ = d.areaNumInQ + d.numInQ * timeSinceLastEvent
    d.areaNumInSystem = d.areaNumInSystem + (d.numInQ + d.serverStatus) * timeSinceLastEvent
    # Update area under server-busy indicator function.
    d.areaServerStatus = d.areaServerStatus + d.serverStatus * timeSinceLastEvent
    d.serverStatusAvgList.append(d.areaServerStatus/d.time)


def main(i, ir, sr, ndr):

    d = Data()
    d.interarrival_rate = ir
    d.service_rate = sr
    d.numDelaysRequired = ndr
    d.iteration = i

    d.qLimit = 10000
    for _ in range(0, d.qLimit+1):
        d.timeArrival.append(0)
        d.numInQList.append(0)
        d.numInSystemList.append(0)

    d.numEvents = 2

    initialize(d)

    while d.numcustsDelayed < d.numDelaysRequired:
        timing(d)
        updateTimeAvgStats(d)
        if d.nextEventType == 0:
            arrive(d)
        else:
            depart(d)
    report(d)

    file = open("serverStatusAvgList_"+str(d.iteration)+".txt", "w+")
    for i in range(0, len(d.serverStatusAvgList)):
        file.write(str(d.serverStatusAvgList[i]) + "\n")
    file.close()

    file = open("timeInQList_"+str(d.iteration)+".txt", "w+")
    for i in range(0, len(d.timeInQList)):
        file.write(str(d.timeInQList[i]) + "\n")
    file.close()

    file = open("timeInSystemList_"+str(d.iteration)+".txt", "w+")
    for i in range(0, len(d.timeInSystemList)):
        file.write(str(d.timeInSystemList[i]) + "\n")
    file.close()

    r = 0
    for i in range(0, len(d.numInQList)):
        if d.numInQList[i] != 0: r = r + d.numInQList[i]
        else: break
    file = open("numInQList_"+str(d.iteration)+".txt", "w+")
    for i in range(0, len(d.numInQList)):
        if d.numInQList[i] != 0:
            file.write(str(i)+": "+ str(d.numInQList[i]/r) + "\n")
        else:
            break
    file.close()

    r = 0
    for i in range(0, len(d.numInSystemList)):
        if d.numInSystemList[i] != 0: r = r + d.numInSystemList[i]
        else: break
    file = open("numInSystemList_"+str(d.iteration)+".txt", "w+")
    for i in range(0, len(d.numInSystemList)):
        if d.numInSystemList[i] != 0:
            file.write(str(i)+": "+ str(d.numInSystemList[i]/r) + "\n")
        else:
            break
    file.close()


interarrival_rate = float(input("Ingrese 'λ': "))  # Tasa de llegada
service_rate = float(input("Ingrese 'μ': "))  # Tasa de servicio
numDelaysRequired = float(input("Ingrese el número de clientes: "))
numExperiments = int(input("Ingrese el número de experimentos: "))

for i in range(1, numExperiments+1):
    main(i, interarrival_rate, service_rate, numDelaysRequired)