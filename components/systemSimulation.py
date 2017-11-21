#Antoine GARGOT - CS 555 - Project

import numpy as np
from components.queue import Queue
from components.customer import Customer
from components.measure import Measure

class SystemSimulation():
 
    def __init__(self, arrival_rate, nb_customers, service_rate, no_of_servers, capacity):
        self.arrival_rate = arrival_rate
        self.queue = Queue(service_rate, no_of_servers, capacity)
        self.nb_customers = nb_customers
        self.customers = {}
        self.measures = {}
        self.nb_of_accepted_customers = 0
        self.time = 0
        for i in range(nb_customers):
            new_customer = Customer(0)
            self.nb_of_accepted_customers += 1
            self.customers[self.nb_of_accepted_customers] = new_customer 
            new_customer.enter_queue(self.queue)
            self.measures[self.time] = Measure(self.customers, self.queue)

    def main_simulation_loop(self, simulation_time, measure = True):
         #In a Poission process the size of the interval between consecutive events is exponential tx = -To*ln(X).
        while self.time < simulation_time:
            self.time -= (1/self.arrival_rate) * np.log(np.random.uniform(0,1))
            self.queue.clean_up_queue(self.time)
            if (len(self.queue.queue) < self.queue.capacity) :
                new_customer = Customer(self.time)
                self.nb_of_accepted_customers += 1
                self.customers[self.nb_of_accepted_customers] = new_customer 
                new_customer.enter_queue(self.queue)
            else :
                print("Customer rejected")
            self.nb_customers += 1
            self.measures[self.time] = Measure(self.customers, self.queue)
        return self.customers, self.measures 


