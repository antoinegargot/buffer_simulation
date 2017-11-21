#Antoine GARGOT - CS 555 - Project

class Customer:
    
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        
    def enter_queue(self, queue):
        next_available_time = min(queue.next_available_times)
        next_available_server = queue.next_available_times.index(next_available_time)

        self.service_time = queue.service_time()

        self.service_start_time = max(self.arrival_time, next_available_time)

        self.service_end_time = self.service_start_time + self.service_time

        self.wait = self.service_end_time - self.arrival_time

        queue.next_available_times[next_available_server] = self.service_end_time
        queue.queue.append(self)
