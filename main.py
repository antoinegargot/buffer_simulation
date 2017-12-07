#Antoine GARGOT - CS 555 - Project
from components.welch import WelchAlgorithm
from components.dataVizualiser import DataVizualiser
import matplotlib.pyplot as plot
from components.systemSimulation import SystemSimulation
import numpy as np
import time

def random_number_generator():
    np.random.seed(int(time.time()))
    first_set = np.random.uniform(0,1,1000000)
    np.random.seed(int(time.time())+ 2000)
    second_set = np.random.uniform(0,1,1000000)
    first_set.sort()
    second_set.sort()
    compare = first_set - second_set
    compare
    np.random.uniform(0,1)

def simple_system_simulation(similation_time, arrival_rate, nb_customers, service_rate, no_of_servers, capacity):
    simulation = SystemSimulation(arrival_rate, nb_customers, service_rate, no_of_servers, capacity)
    customers, measures = simulation.main_simulation_loop(similation_time)
    data = [measures[time].system_length for time in [measure for measure in measures]]
    plot.plot(data)
    plot.grid()
    plot.xlim([0,similation_time])
    plot.xlabel('Time')
    plot.ylabel('Customers in the system')
    plot.show()
    
def elimination_of_warmup_period(similation_time, arrival_rate, nb_customers, service_rate, no_of_servers, capacity, simulation_nb, window):
    simulation = WelchAlgorithm(simulation_nb, window, similation_time)
    mean_measures, welch_measure = simulation.launch(arrival_rate, nb_customers, service_rate, no_of_servers, capacity)
    plot.figure()
    plot.plot(mean_measures, label='Mean mesures of simulations')
    plot.plot(welch_measure, label='Welch algorithm of the simulation')
    plot.grid()
    plot.legend(loc='best')
    plot.xlim([0,similation_time])
    plot.xlabel('Time')
    plot.ylabel('Customers in the system')
    plot.show()

def batch_measure(similation_time, arrival_rate, nb_customers, service_rate, no_of_servers, capacity, warmmup_period , batch_size):
    simulation = SystemSimulation(arrival_rate, nb_customers, service_rate, no_of_servers, capacity, True, warmmup_period , batch_size)
    customers, batch_measures = simulation.main_simulation_loop(similation_time)
    total_nb_of_accepted_customers = []
    total_nb_customers = []
    system_size = []
    simulation_mean_system_size = []
    average_wait = []
    for batch_measure in batch_measures:
        total_nb_of_accepted_customers.append(len(batch_measures[batch_measure]["customers"]))
        total_nb_customers.append(batch_measures[batch_measure]["nb_customers"])
        for customers in [batch_measures[batch_measure]["customers"]]:
            average_wait.append(float(sum(customers[ID].wait for ID in customers)) / max(len(customers), 1))
        for measure in [batch_measures[batch_measure]["measures"]]:
            for data in measure:
                system_size.append(measure[data].system_length)
            simulation_mean_system_size.append(float(sum(system_size)/len(system_size)))
            system_size = []
    return total_nb_of_accepted_customers, total_nb_customers, simulation_mean_system_size, average_wait