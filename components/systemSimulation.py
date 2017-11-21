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
        self.nb_of_accepted_customers = 0

        for i in range(0,nb_customers):
            new_customer = Customer(0)
            self.nb_of_accepted_customers += 1
            self.customers[self.nb_customers] = new_customer 
            new_customer.enter_queue(self.queue)
            
    def main_simulation_loop(self, simulation_time, measure = True):
        time = 0
        measures = {}
         #In a Poission process the size of the interval between consecutive events is exponential tx = -To*ln(X).
        time -= (1/self.arrival_rate) * np.log(np.random.uniform(0,1))
        while time < simulation_time:
            self.nb_customers += 1

            if (self.queue.customers_in_queue <= self.queue.capacity) :
                new_customer = Customer(time)
                self.nb_of_accepted_customers += 1
                self.customers[self.nb_of_accepted_customers] = new_customer 
                
                new_customer.enter_queue(self.queue)
                self.queue.clean_up_queue(time)
                time -= (1/self.arrival_rate) * np.log(np.random.uniform(0,1))
    
                if measure:
                    measures[time] = Measure(self.customers, self.queue)
            else :
                print("Customer rejected")
        
        return self.customers, measures 


