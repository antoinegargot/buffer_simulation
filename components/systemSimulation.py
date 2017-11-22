#Antoine GARGOT - CS 555 - Project

import numpy as np
from components.queue import Queue
from components.customer import Customer
from components.measure import Measure

class SystemSimulation():
 
    def __init__(self, arrival_rate, nb_customers, service_rate, no_of_servers, capacity):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.queue = Queue(service_rate, no_of_servers, capacity)
        self.nb_customers = nb_customers
        self.customers = {}
        self.measures = {}
        self.nb_of_accepted_customers = 0
        self.arrival_time = 0
        self.current_time = 0
        #simulation_interval for measure is :
        self.simulation_interval = min(1/self.arrival_rate, 1/self.service_rate)
        for i in range(nb_customers):
            new_customer = Customer(0)
            self.nb_of_accepted_customers += 1
            self.customers[self.nb_of_accepted_customers] = new_customer 
            new_customer.enter_queue(self.queue)
            self.queue.clean_up_queue(self.arrival_time)
            self.measures[self.arrival_time] = Measure(self.customers, self.queue)


    def main_simulation_loop(self, simulation_time, measure = True):
         #In a Poission process the size of the interval between consecutive events is exponential tx = -To*ln(X).
        self.arrival_time -= (1/self.arrival_rate) * np.log(np.random.uniform(0,1))
        #Symulation clock with 0.001 accuracy level
        while self.current_time < simulation_time:
            self.queue.clean_up_queue(self.current_time)
            if (self.current_time >= self.arrival_time):
                if (len(self.queue.queue) < self.queue.capacity) :
                    new_customer = Customer(self.arrival_time)
                    self.nb_of_accepted_customers += 1
                    self.customers[self.nb_of_accepted_customers] = new_customer 
                    new_customer.enter_queue(self.queue)
                    self.nb_customers += 1
                self.arrival_time -= (1/self.arrival_rate) * np.log(np.random.uniform(0,1))
            if (self.current_time >= self.simulation_interval) :
                self.measures[self.simulation_interval] = Measure(self.customers, self.queue)
                self.simulation_interval += min(1/self.arrival_rate, 1/self.service_rate)
            self.current_time += 0.001
        return self.customers, self.measures 