#Antoine GARGOT - CS 555 - Project
class Measure:
   
    def __init__(self, customers, queue):
    	#Measure of the system lenght in a specific time 
        self.system_length = len(queue.queue)
