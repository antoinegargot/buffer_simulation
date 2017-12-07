#Antoine GARGOT - CS 555 - Project

import numpy as np
import random

class Queue:
    def __init__(self, service_rate, nb_of_servers = 2, capacity = 5):

        #Apply the service rate for the systme into the queue in order to 
        self.service_rate = service_rate

        #Create an array of n floats (number of servers in the system), each number in the array will correspond to the future available time of a server.
        self.next_available_times = [0 for server in range(nb_of_servers)]

        #The capacity of the system
        self.capacity = capacity

        #Define the array of customers in the system.
        self.queue = []

    def service_time(self):
        #Compute a potential service time for one customer
        return (-(1/self.service_rate) * np.log(np.random.uniform(0,1)))
    
    def clean_up_queue(self, time):
        newQueue = []
        #Recreate the queue based on customers that will be served in the future in the system.
        for customer in self.queue :
            if (customer.service_end_time >= time) :
                newQueue.append(customer)
        self.queue = newQueue