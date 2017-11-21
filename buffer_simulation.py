#Antoine GARGOT - CS 555 - Project
import matplotlib.pyplot as plot
import numpy as np
from SystemSimulation import SystemSimulation

#1. (15%) Test your random number generator (RNG):
##Let's use the numpy library for Python in order to generate random numbers sample.

#1.1 Does your RNG generate random numbers?

##Let's create a sample of 200 random variables in order to check if our RNG generate random numbers
randomSample = np.random.randn(200)
print(randomSample)
#Our basic configuration of our RNG generate an array of random variable.

#Let's plot our array :
plot.hist(randomSample)
plot.title("Random sample Histogram")
plot.xlabel("Value")
plot.ylabel("Frequency")
fig = plot.gcf()

#1.2 How do you initialize the seed of your RNG?
#The seed is a starting point in a sequence of RNG. We can set it simply by calling the seed function of numpy as bellow :
np.random.seed(1234)

#1.3 Generate two sequences of 1000000 numbers each, for every sequence use a different seed. Are these two sequences different? How do you know this?
randomSample1 = np.random.randn(10000)
np.random.seed(4000)
randomSample2 = np.random.randn(10000)
n, bins, patches = plot.hist([randomSample1, randomSample2])
#As the random function is normally distributed and each sample has 10000 observations, the sequence when we start does not affect the global repartission of our data (deterministic behavior).
#The distribution of those two sample are barely the same for each different simulation due to the previous explanation.

#2. (30%) Eliminate the warm-up period separately for each of the following cases by applying the Welch graphical procedure:
if __name__ == '__main__':
    simulation_time = eval(arguments['<time>'])
#2.1 System A with the initial condition x(t=0)=0, i.e. the system is empty at t=0.
    A1 = SimulationModel(1, 0, 1, 2, 5)
    customersA1, snapsA1 = A1.main_simulation_loop(simulation_time, measure = True)
    
#2.2 System A with the initial condition x(t=0)=7, i.e. the system is full at t=0.
    A2 = SimulationModel(1, 7, 1, 2, 5)
    customersA2, snapsA2 = A2.main_simulation_loop(simulation_time, measure = True)

#2.3 System B with the initial condition x(t=0)=0, i.e. the system is empty at t=0.
    B1 = SimulationModel(1, 0, 1, 2, 5)
    customersB1, snapsB1 = B1.main_simulation_loop(simulation_time, measure = True)

#2.4 System B with the initial condition x(t=0)=4, i.e. there are 4 customers in the system at t=0.
    B2 = SimulationModel(10, 4, 1, 2, 5)
    customersB2, snapsB2 = B2.main_simulation_loop(simulation_time, measure = True)



