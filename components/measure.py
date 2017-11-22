#Antoine GARGOT - CS 555 - Project
class Measure:
   
    def __init__(self, customers, queue):
        self.system_length = len(queue.queue)
        self.average_wait = float(sum(customers[ID].wait for ID in customers)) / max(len(customers), 1)
