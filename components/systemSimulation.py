#Antoine GARGOT - CS 555 - Project

import numpy as np
from components.queue import Queue
from components.customer import Customer
from components.measure import Measure

class SystemSimulation():
 
    def __init__(self, arrival_rate, nb_customers, service_rate, no_of_servers, capacity, is_batch = False, warmmup_period = 0, batch_size = 0):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.queue = Queue(service_rate, no_of_servers, capacity)
        self.nb_customers = nb_customers
        self.no_of_servers = no_of_servers
        self.customers = {}
        self.measures = {}
        self.nb_of_accepted_customers = 0
        self.arrival_time = 0
        self.current_time = 0
        self.is_batch = is_batch
        self.warmmup_period = warmmup_period
        self.batch_size = batch_size
        #simulation_interval for measure is :
        if (self.is_batch):
            self.simulation_interval = min(1/self.arrival_rate, 1/self.service_rate) + self.warmmup_period
        else :
            self.simulation_interval = min(1/self.arrival_rate, 1/self.service_rate)

        for i in range(nb_customers):
            new_customer = Customer(0)
            self.nb_of_accepted_customers += 1
            self.customers[self.nb_of_accepted_customers] = new_customer 
            new_customer.enter_queue(self.queue)
            self.queue.clean_up_queue(self.arrival_time)
        if (not self.is_batch):
            self.measures[0.0] = Measure(self.customers, self.queue)


    def main_simulation_loop(self, simulation_time, measure = True):
         #In a Poission process the size of the interval between consecutive events is exponential tx = -To*ln(X).
        self.arrival_time -= (1/self.arrival_rate) * np.log(np.random.uniform(0,1))
        self.batch_measures = {}
        batch_measure = {}
        batch_interval = self.batch_size + self.warmmup_period
        n = 0;
        #Symulation clock with 0.001 accuracy level
        while self.current_time < simulation_time:
            self.queue.clean_up_queue(self.current_time)
          
            if (self.current_time >= self.arrival_time):
                if (len(self.queue.queue) < self.queue.capacity + self.no_of_servers) :
                    new_customer = Customer(self.arrival_time)
                    self.nb_of_accepted_customers += 1
                    self.customers[self.nb_of_accepted_customers] = new_customer 
                    new_customer.enter_queue(self.queue)

                self.nb_customers += 1
                self.arrival_time -= (1/self.arrival_rate) * np.log(np.random.uniform(0,1))

            if ((not self.is_batch) or (self.is_batch and (self.current_time >= self.warmmup_period))):
                if (self.current_time >= self.simulation_interval) :
                    self.measures[self.simulation_interval] = Measure(self.customers, self.queue)
                    self.simulation_interval += min(1/self.arrival_rate, 1/self.service_rate)

            if (self.is_batch and (self.current_time <= self.warmmup_period)):
                #Reset counters before captures for batch method
                self.nb_of_accepted_customers = 0
                self.nb_customers = 0
                self.customers = {}

            if (self.is_batch and (self.current_time >= self.warmmup_period) and (self.current_time >= batch_interval)):
                    batch_measure["measures"] = self.measures
                    batch_measure["customers"] = self.customers
                    batch_measure["nb_customers"] = self.nb_customers
                    self.batch_measures[n] = batch_measure
                    n += 1
                    self.measures = {}
                    batch_measure = {}
                    self.nb_of_accepted_customers = 0
                    self.nb_customers = 0
                    self.customers = {}
                    batch_interval += self.batch_size
            self.current_time += 0.001
        if (self.is_batch):
            return self.customers, self.batch_measures
        else:
            return self.customers, self.measures 



