#Antoine GARGOT - CS 555 - Project
import matplotlib.pyplot as plot
import numpy as np
from components.systemSimulation import SystemSimulation
from components.dataVizualiser import DataVizualiser

#1. (15%) Test your random number generator (RNG):
##Let's use the numpy library for Python in order to generate random numbers sample.

#1.1 Does your RNG generate random numbers?

##Let's create a sample of 10 000 uniform random variables in order to check if our RNG generate uniform random numbers between 0 and 1
randomSample =  np.random.uniform(0,1,10000)
print(randomSample)
#Our basic configuration of our RNG generate an array of random variable.

#Let's plot our array :

plot.hist(randomSample, bins =1000)
plot.title("Uniform random sample Histogram")
plot.xlabel("Value")
plot.ylabel("Frequency")
plot.show()

#draw the PDF and CDF (CDF should be linear) 
#By changing seed we will not have the same sample 
#Bar graph scale (0.001)
#1.2 How do you initialize the seed of your RNG?
#The seed is a starting point in a sequence of RNG. We can set it simply by calling the seed function of numpy as bellow :
#Time is a good way to change the seed.
np.random.seed(1234)

#1.3 Generate two sequences of 1000000 numbers each, for every sequence use a different seed. Are these two sequences different? How do you know this?
randomSample1 = np.random.randn(10000)
np.random.seed(4000)
randomSample2 = np.random.randn(10000)
n, bins, patches = plot.hist([randomSample1, randomSample2])
#As the random function is normally distributed and each sample has 10000 observations, the sequence when we start does not affect the global repartission of our data (deterministic behavior).
#The distribution of those two sample are different for each different simulation due to the previous explanation.
#Find a way to proof the difference between those two samples.

#2. (30%) Eliminate the warm-up period separately for each of the following cases by applying the Welch graphical procedure:
if __name__ == '__main__':
    simulation_time = 10#eval(arguments['<time>'])
#2.1 System A with the initial condition x(t=0)=0, i.e. the system is empty at t=0.
    A1 = SystemSimulation(1, 0, 1, 2, 5)
    customersA1, measuresA1 = A1.main_simulation_loop(simulation_time, measure = True)
    
#2.2 System A with the initial condition x(t=0)=7, i.e. the system is full at t=0.
    A2 = SystemSimulation(1, 7, 1, 2, 5)
    customersA2, measuresA2 = A2.main_simulation_loop(simulation_time, measure = True)

#2.3 System B with the initial condition x(t=0)=0, i.e. the system is empty at t=0.
    B1 = SystemSimulation(10, 0, 1, 2, 5)
    customersB1, measuresB1 = B1.main_simulation_loop(simulation_time, measure = True)

#2.4 System B with the initial condition x(t=0)=4, i.e. there are 4 customers in the system at t=0.
    B2 = SystemSimulation(10, 4, 1, 2, 5)
    customersB2, measuresB2 = B2.main_simulation_loop(simulation_time, measure = True)
    
#100 replication per simulation at least.
    Graph = DataVizualiser()
    Graph.plot_length(measuresA1)


