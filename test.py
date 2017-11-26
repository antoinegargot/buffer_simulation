#Antoine GARGOT - CS 555 - Project
from components.welch import WelchAlgorithm
from components.dataVizualiser import DataVizualiser
import matplotlib.pyplot as plot
from components.systemSimulation import SystemSimulation

def random_number_generator():
    print("TODO")
    return 0

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
    return 0
    
def elimination_of_warmup_period(similation_time, arrival_rate, nb_customers, service_rate, no_of_servers, capacity, simulation_nb, window):
    simulation = WelchAlgorithm(10, window, similation_time)
    mean_measures, welch_measure = simulation.launch(arrival_rate, nb_customers, service_rate, no_of_servers, capacity)
    plot.plot(mean_measures)
    plot.plot(welch_measure)
    plot.grid()
    plot.legend(['Mean mesures of simulations', 'Welch algorithm of the simulation'], loc='upper left')
    plot.xlim([0,similation_time])
    plot.xlabel('Time')
    plot.ylabel('Customers in the system')
    plot.show()
    return 0

def batch_measure(similation_time, arrival_rate, nb_customers, service_rate, no_of_servers, capacity, warmmup_period , batch_size):
    simulation = SystemSimulation(similation_time, arrival_rate, nb_customers, service_rate, no_of_servers, capacity, True, warmmup_period , batch_size)
    customers, batch_measures = simulation.main_simulation_loop(similation_time)
    total_nb_of_accepted_customers = []
    total_nb_customers = []
    system_size = []
    average_wait = []
    for batch_measure in batch_measures:
        total_nb_of_accepted_customers.append(len(batch_measures[batch_measure]["customers"]))
        total_nb_customers.append(batch_measures[batch_measure]["nb_customers"])
        for customers in [batch_measures[batch_measure]["customers"]]:
            average_wait.append(float(sum(customers[ID].wait for ID in customers)) / max(len(customers), 1))
        for measure in [batch_measures[batch_measure]["measures"]]:
            for data in measure:
                system_size.append(measure[data].system_length)
    plot.bar(system_size)
    plot.grid()
    plot.xlim([0,similation_time])
    plot.xlabel('Time')
    plot.ylabel('Customers in the system')
    plot.show()
    return total_nb_of_accepted_customers, total_nb_customers, system_size, average_wait
