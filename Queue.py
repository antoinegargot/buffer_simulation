#Antoine GARGOT - CS 555 - Project

from Customer import Customer

class Queue:
    def __init__(self, service_rate, nb_of_servers = 2, capacity = 5, customers_in_queue = 0):
        self.service_rate = service_rate
        self.next_available_times = [0 for server in range(nb_of_servers)]
        self.capacity = capacity
        self.customers_in_queue = customers_in_queue
        self.queue = []

    def service_time(self):
        return (-(1/self.service_rate) * np.ln(np.random.uniform(0,1)))
    
    def clean_up_queue(self, time):
        self.queue = [Customer for Customer in self.queue if Customer.service_end_time > time]