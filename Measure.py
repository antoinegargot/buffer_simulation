#Antoine GARGOT - CS 555 - Project
class Measure:
   
    def __init__(self, customers, queue):
        self.queue_length = len(queue.queue)
        self.average_wait = sum(customers[ID].wait for ID in customers )/len(customers)