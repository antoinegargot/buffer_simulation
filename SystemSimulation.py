#Antoine GARGOT - CS 555 - Project

from Queue import Queue
from Customer import Customer
from Measure import Measure
import numpy as np

class SystemSimulation():
 
    def __init__(self, arrival_rate, nb_customers = 0, service_rate, no_of_servers, capacity):
        self.arrival_rate = arrival_rate
        self.queue = Queue(service_rate, no_of_servers, capacity)
        self.nb_customers = nb_customers
        self.customers = {}
        self.nb_of_accepted_customers = 0

        for i in range(nb_customers) {
            new_customer = Customer(0)
            self.nb_of_accepted_customers += 1
            self.customers[self.no_of_customers] = new_customer 
            new_customer.enter_queue(self.queue)
        }
            
    def main_simulation_loop(self, simulation_time, measure = True):
        time = 0
        measures = {}
         #In a Poission process the size of the interval between consecutive events is exponential tx = -To*ln(X).
        time -= (1/self.arrival_rate) * np.ln(np.random.uniform(0,1))
        while time < simulation_time:
            self.no_of_customers += 1

            if (queue.customers_in_queue <= queue.capacity) {
                new_customer = Customer(time)
                self.nb_of_accepted_customers += 1
                self.customers[self.nb_of_accepted_customers] = new_customer 
                
                new_customer.enter_queue(self.queue)
                self.queue.clean_up_queue(time)
                time -= (1/self.arrival_rate) * np.ln(np.random.uniform(0,1))
    
                if measure:
                    measures[time] = Measure(customers, self.queue)
            else {
                print("Customer rejected")
            }
        
        return self.customers, measures 
