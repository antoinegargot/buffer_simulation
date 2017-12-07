#Antoine GARGOT - CS 555 - Project

class Customer:
    
    def __init__(self, arrival_time):

        #Define the arrival time of the customer in the system.
        self.arrival_time = arrival_time
        
    def enter_queue(self, queue):
        #We will take the future available service time slot (in the array of servers)
        next_available_time = min(queue.next_available_times)

        #We will take the index of the future available slot in the array
        next_available_server = queue.next_available_times.index(next_available_time)

        #Let's calculate a new service time from the service rate.
        self.service_time = queue.service_time()

        #Attach to the customer, the time when he will be served.
        self.service_start_time = max(self.arrival_time, next_available_time)

        #Attach to the customer is departure time from the system.
        self.service_end_time = self.service_start_time + self.service_time

        #Define the waiting time of the customer in the system. 
        self.wait = self.service_end_time - self.arrival_time

        #Define the new available time for the targeted server.
        queue.next_available_times[next_available_server] = self.service_end_time
        
        queue.queue.append(self)
