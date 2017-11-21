#Antoine GARGOT - CS 555 - Project

import numpy as np
import random

class Queue:
    def __init__(self, service_rate, nb_of_servers = 2, capacity = 5):
        self.service_rate = service_rate
        self.next_available_times = [0 for server in range(nb_of_servers)]
        self.capacity = capacity
        self.queue = []

    def service_time(self):
        return (-(1/self.service_rate) * np.log(np.random.uniform(0,1)))
    
    def clean_up_queue(self, time):
        newQueue = []
        for customer in self.queue :
            if (customer.service_end_time > time) :
                newQueue.append(customer)
        self.queue = newQueue